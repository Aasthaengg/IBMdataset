#!/usr/bin/env python3
H, W = map(int, input().split())
M = [list(input()) for _ in range(H)]

# yoko
for i in range(H):
    for j in range(W-1):
        if (M[i][j] == '#' or M[i][j] == 'M') and (M[i][j+1] == '#' or M[i][j+1] == 'M'):
            M[i][j] = 'M'
            M[i][j+1] = 'M'

#tate
for j in range(W):
    for i in range(H-1):
        if (M[i][j] == '#' or M[i][j] == 'M') and (M[i+1][j] == '#' or M[i+1][j] == 'M'):
            M[i][j] = 'M'
            M[i+1][j] = 'M'

ret = 0
for m in M:
    ret += m.count('#')

if ret == 0: print('Yes')
else: print('No')
