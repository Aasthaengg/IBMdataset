#!/usr/bin/env python3
from collections import deque
h, w = map(int, input().split())
s = []
a = 0
for _ in range(h):
    s.append(list(input()))
mx = [1,-1,0,0]
my = [0,0,1,-1]
for i in range(h):
    for j in range(w):
        if s[i][j] == '.':
            d = [[-1 for a in range(w)] for b in range(h)]
            d[i][j] = 0
            q = deque([(j,i)])
            while q:
                x, y = q.popleft()
                for c in range(4):
                    new_x = x + mx[c]
                    new_y = y + my[c]
                    if 0<=new_x<=w-1 and 0<=new_y<=h-1 and s[new_y][new_x] != "#" and d[new_y][new_x] < 0:
                        q.append((new_x,new_y))
                        d[new_y][new_x] = d[y][x] + 1
                        a = max(a, d[new_y][new_x])
                        
print(a)