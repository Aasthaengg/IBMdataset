import sys
import heapq
import re
from itertools import permutations
from bisect import bisect_left, bisect_right
from collections import Counter, deque
from fractions import gcd
from math import factorial, sqrt, ceil
from functools import lru_cache, reduce
INF = 1 << 60
MOD = 1000000007
sys.setrecursionlimit(10 ** 7)

# UnionFind
class UnionFind():
    def __init__(self, n):
        self.n = n
        self.parents = [-1] * n

    def find(self, x):
        if self.parents[x] < 0:
            return x
        else:
            self.parents[x] = self.find(self.parents[x])
            return self.parents[x]

    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)

        if x == y:
            return

        if self.parents[x] > self.parents[y]:
            x, y = y, x

        self.parents[x] += self.parents[y]
        self.parents[y] = x

    def size(self, x):
        return -self.parents[self.find(x)]

    def same(self, x, y):
        return self.find(x) == self.find(y)

    def members(self, x):
        root = self.find(x)
        return [i for i in range(self.n) if self.find(i) == root]

    def roots(self):
        return [i for i, x in enumerate(self.parents) if x < 0]

    def group_count(self):
        return len(self.roots())

    def all_group_members(self):
        return {r: self.members(r) for r in self.roots()}

    def __str__(self):
        return '\n'.join('{}: {}'.format(r, self.members(r)) for r in self.roots())

def is_prime(n):
    if n == 1:
        return False
    for i in range(2,int(n**0.5)+1):
        if n % i == 0:
            return False
    return True


# ワーシャルフロイド (任意の2頂点の対に対して最短経路を求める)
# 計算量n^3 (nは頂点の数)
def warshall_floyd(d, n):
    #d[i][j]: iからjへの最短距離
    for k in range(n):
        for i in range(n):
            for j in range(n):
                d[i][j] = min(d[i][j],d[i][k] + d[k][j])
    return d


# ダイクストラ
def dijkstra_heap(s, edge, n):
    #始点sから各頂点への最短距離
    d = [10**20] * n
    used = [True] * n #True:未確定
    d[s] = 0
    used[s] = False
    edgelist = []
    for a,b in edge[s]:
        heapq.heappush(edgelist,a*(10**6)+b)
    while len(edgelist):
        minedge = heapq.heappop(edgelist)
        #まだ使われてない頂点の中から最小の距離のものを探す
        if not used[minedge%(10**6)]:
            continue
        v = minedge%(10**6)
        d[v] = minedge//(10**6)
        used[v] = False
        for e in edge[v]:
            if used[e[1]]:
                heapq.heappush(edgelist,(e[0]+d[v])*(10**6)+e[1])
    return d

# 素因数分解
def factorization(n):
    arr = []
    temp = n
    for i in range(2, int(-(-n**0.5//1))+1):
        if temp%i==0:
            cnt=0
            while temp%i==0:
                cnt+=1
                temp //= i
            arr.append([i, cnt])

    if temp!=1:
        arr.append([temp, 1])

    if arr==[]:
        arr.append([n, 1])

    return arr

# 2数の最小公倍数
def lcm(x, y):
    return (x * y) // gcd(x, y)

# リストの要素の最小公倍数
def lcm_list(numbers):
    return reduce(lcm, numbers, 1)

# リストの要素の最大公約数
def gcd_list(numbers):
    return reduce(gcd, numbers)

# 素数判定



# limit以下の素数を列挙
def eratosthenes(limit):
    A = [i for i in range(2, limit+1)]
    P = []

    while True:
        prime = min(A)
        
        if prime > sqrt(limit):
            break
            
        P.append(prime)
            
        i = 0
        while i < len(A):
            if A[i] % prime == 0:
                A.pop(i)
                continue
            i += 1
            
    for a in A:
        P.append(a)
            
    return P

# 同じものを含む順列
def permutation_with_duplicates(L):

    if L == []:
        return [[]]

    else:
        ret = []

        # set（集合）型で重複を削除、ソート
        S = sorted(set(L))

        for i in S:

            data = L[:]
            data.remove(i)

            for j in permutation_with_duplicates(data):
                ret.append([i] + j)

        return ret


# ここから書き始める
N, W = map(int, input().split())
v = [[] for i in range(4)]
w1 = 0
for i in range(N):
    a, b = map(int, input().split())
    if i == 0:
        w1 = a
    v[a - w1].append(b)
for i in range(4):
    v[i].sort(reverse=True)
# print(v)
ans = 0
for i in range(N + 1):
    for j in range(N - i + 1):
        for k in range(N - i - j + 1):
            for l in range(N - i - j - k + 1):
                if w1 * (i + j + k + l) + j + 2 * k + 3 * l > W:
                    continue
                ans = max(ans, sum(v[0][:i]) + sum(v[1][:j]) + sum(v[2][:k]) + sum(v[3][:l]))
print(ans)


