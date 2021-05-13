import sys
import itertools
sys.setrecursionlimit(1000000000)
from heapq import heapify,heappop,heappush,heappushpop
import math
import collections
import copy

def bfs(start):
    d = [-1]*n
    d[start] = 0
    q = collections.deque([start])
    while q:
        p = q.popleft()
        next_v = edge[p]
        for v in next_v:
            if d[v] == -1:
                q.append(v)
                d[v] = d[p] + 1
    return d

if __name__ == "__main__":
    n = int(input())
    edge = []
    for i in range(n):
        u,k,*v_li = map(int,input().split())
        u-=1
        for j in range(len(v_li)):
            v_li[j] -= 1
        edge.append(v_li)
    ans = bfs(0)
    for i in range(n):
        print(i+1,ans[i])

