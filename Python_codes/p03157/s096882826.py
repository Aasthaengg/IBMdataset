from itertools import*
import math
from collections import*
from heapq import*
from bisect import bisect_left,bisect_right
from copy import deepcopy
inf = 10**18
mod = 10**9+7
from functools import reduce
import sys
sys.setrecursionlimit(10**7)

H,W  = map(int,input().split())
S = [input() for i in range(H)]

dirc = [(0,1),(1,0),(0,-1),(-1,0)]
visited = [[False]*W for _ in range(H)]

def bfs(i,j):
    b,w = 0,0
    visited[i][j] = True
    que = deque([(i,j)])

    while que:
        ci,cj = que.popleft()
        if S[ci][cj] =="#":
            b += 1
        else:
            w += 1

        for di,dj in dirc:
            ni,nj = ci+di,cj+dj
            if not(0<=ni<H and 0<=nj<W) or visited[ni][nj]:
                continue
            if S[ci][cj] != S[ni][nj]:
                visited[ni][nj] = True
                que.append((ni,nj))
    return b*w

res = 0
for i in range(H):
        for j in range(W):
            if visited[i][j]:
                continue
            res += bfs(i,j)
print(res)