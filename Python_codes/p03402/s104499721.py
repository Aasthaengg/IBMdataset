# -*- coding: utf-8 -*-
#D - Grid Components
import sys 
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
A,B = map(int,readline().split())
grid = []
for _ in range(50):
    grid.append(['.']*100)
for _ in range(50):
    grid.append(['#']*100)   
A -= 1
B -= 1

cnt = 0
f = 0
for i in range(1,50,2):
    for j in range(1,99,2):
        if cnt == B:
            f = 1
            break
        cnt += 1
        grid[i][j] = '#'
    if f == 1:
        break
cnt = 0
f = 0
for i in range(51,100,2):
    for j in range(1,99,2):
        if cnt == A:
            f = 1
            break
        cnt += 1
        grid[i][j] = '.'
    if f == 1:
        break
print(100,100)
for row in grid:
    print(''.join(a for a in row)) 