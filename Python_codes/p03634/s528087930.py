import sys
import heapq
from itertools import permutations
from bisect import bisect_left, bisect_right
from collections import Counter, deque
from fractions import gcd
from math import factorial, sqrt
INF = 1 << 60
sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline

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

def dijkstra_heap(s,edge):
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
# def dfs(current, goal, cost, visited):
#     if current == goal:
#         return cost
#     if len(tree[current]) == 0:
#         return 0 
#     for i in tree[current]:
#         # print("i =", i)
#         if visited[i[0]] == 0:
#             return dfs(i[0], goal, cost + i[1])

def bfs(queue):
    visited = [0] * n
    while queue:
        # print("dist =", dist)
        node = queue.popleft()
        # print("node =", node)
        current = node[0]
        if visited[current] == 0:
            new_cost = node[1]
            cost = node[2]
            cost += new_cost
            dist[current] = min(dist[current], cost)
            visited[current] = 1
            for i in tree[current]:
                queue.append([i[0], i[1], cost])

n = int(input())
tree = [[] for i in range(n)]
for i in range(n - 1):
    a, b, c = map(int, input().split())
    a -= 1
    b -= 1
    tree[a].append([b, c])
    tree[b].append([a, c])
# print(tree)
q, k = map(int, input().split())
k -= 1
dist = [INF] * n
# visited = [0] * n
queue = deque([[k, 0, 0]])
# print(queue)
bfs(queue)
# print("dist =", dist)
ans = [0] * q
for i in range(q):
    x, y = map(int, input().split())
    x -= 1
    y -= 1
    ans[i] = dist[x] + dist[y]
for i in ans:
    print(i)
