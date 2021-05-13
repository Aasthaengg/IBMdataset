#!/usr/bin/env python3

H,W = [int(i) for i in input().split()]
S = []
S.append('.'*(W+2))
for i in range(H):
    S.append('.'+input()+'.')
S.append(['.']*(W+2))

for y in range(1,H+1):
    for x in range(1,W+1):
        if S[y][x] == '#':
            print('#',end="")
        else:
            print(S[y-1][x-1:x+2].count('#')+S[y][x-1:x+2].count('#')+S[y+1][x-1:x+2].count('#'),end="")
    print("")
