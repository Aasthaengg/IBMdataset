import sys
input = sys.stdin.readline
from collections import *

H, W = map(int, input().split())
A = [list(input()[:-1]) for _ in range(H)]
l = []

for i in range(H):
    for j in range(W):
        if A[i][j]=='#':
            l.append((i, j))
    
ans = 0

while True:
    nl = []
    
    for x, y in l:
        for nx, ny in [(x-1, y), (x+1, y), (x, y-1), (x, y+1)]:
            if 0<=nx<H and 0<=ny<W and A[nx][ny]=='.':
                nl.append((nx, ny))
                A[nx][ny] = '#'
    
    if len(nl)==0:
        break
    
    l = nl
    ans += 1

print(ans)