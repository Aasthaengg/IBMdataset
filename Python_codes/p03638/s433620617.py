import sys
from heapq import heappush, heappop, heappushpop, heapify, heapreplace
from itertools import permutations
from bisect import bisect_left, bisect_right
from collections import Counter, deque
from fractions import gcd
from math import factorial, sqrt
INF = 1 << 60
sys.setrecursionlimit(10 ** 6)

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

#ここから書き始める
h, w = map(int, input().split())
n = int(input())
a = list(map(int, input().split()))

cnt = 0
ans = [[0 for j in range(w)] for i in range(h)]
for i in range(1, n + 1):
    for j in range(a[i - 1]):
        ans[cnt // w][cnt % w] = i
        cnt += 1
# print(ans)
for i in range(h):
    if i % 2 == 1:
        ans[i] = ans[i][::-1]
# print(ans)
for i in range(h):
    for j in range(w):
        print(ans[i][j], end=" ")
    print()


