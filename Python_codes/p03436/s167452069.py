import sys
import math
import collections
import decimal
import itertools
from collections import deque
from functools import reduce
import heapq
#m = int(input())
h, w = map(int, sys.stdin.readline().split())
#s = input()
#a = list(map(int, sys.stdin.readline().split()))

black = 0
l = []
l.append(["#"] * (w+2))
for i in range(h):
    z = list(input())
    
    for j in range(len(z)):
        if z[j] == "#":
            black += 1
            
    z.append("#")
    z.insert(0, "#")
    l.append(z)
    
l.append(["#"] * (w+2))

q = deque([])
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
f = [[float("INF") for i in range(w+2)] for j in range(h+2)]

q.append((1, 1, 0))
f[1][1] = 0
while q:
    y, x, cnt = q.popleft()
    if y == h and x == w:
        print(h * w - black - cnt - 1)
        sys.exit()
    
    for i in range(4):
        if l[y+dy[i]][x+dx[i]] == "." and f[y+dy[i]][x+dx[i]] != 0:
            q.append((y+dy[i], x+dx[i], cnt+1))
            f[y+dy[i]][x+dx[i]] = 0

print(-1)
            
            
    
    











