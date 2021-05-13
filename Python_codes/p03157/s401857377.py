import bisect
import collections
import copy
import functools
import heapq
import math
import sys
from collections import deque
from collections import defaultdict
input = sys.stdin.readline
sys.setrecursionlimit(10**9)
MOD = 10**9+7

H,W = map(int,input().split())

S = [list(input()) for i in range(H)]

dx = [1,-1,0,0]
dy = [0,0,1,-1]

start = []
for i in range(H):
    for j in range(W):
        if S[i][j] == "#":
            start.append((i,j))

not_visited = [[-1]*W for i in range(H)]
def distance(i,j):
    not_visited[i][j] = 0
    stack = deque()
    stack.append((i,j,"#"))

    b,w = 1,0

    while stack != deque([]):
        y,x,mark = stack.popleft()
        for i in range(4):
            if 0<= x+dx[i] <W and 0<= y+dy[i] <H and mark != S[y+dy[i]][x+dx[i]]  and not_visited[y+dy[i]][x+dx[i]] == -1:
                not_visited[y+dy[i]][x+dx[i]] =  not_visited[y][x] + 1
                if mark == "#":
                    stack.append((y+dy[i],x+dx[i],"."))
                    w += 1
                else:
                    stack.append((y+dy[i],x+dx[i],"#"))
                    b += 1
    
    return b*w

ans = 0
for i in range(H):
    for j in range(W):
        if not_visited[i][j] == -1 and S[i][j] == "#":
            ans += distance(i,j)
print(ans)