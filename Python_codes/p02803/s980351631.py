import os, sys, re, math


(H, W) = [int(n) for n in input().split()]


def set_moves(x, y, moves):
    if S[y + 1][x + 1] != '.':
        return
    if 0 <= grid[y][x] < moves:
        return

    grid[y][x] = moves
    set_moves(x, y - 1, moves + 1)
    set_moves(x, y + 1, moves + 1)
    set_moves(x - 1, y, moves + 1)
    set_moves(x + 1, y, moves + 1)


S = []
S.append('#' * (W + 2))
has_wall = False
for i in range(H):
    s = input()
    has_wall |= '#' in s
    S.append('#' + s + '#')
S.append('#' * (W + 2))

if not has_wall:
    result = W + H - 2
else:
    result = 0
    for gy in range(H):
        for gx in range(W):
            if S[gy + 1][gx + 1] != '.':
                continue
            grid = []
            for i in range(H):
                grid.append([-1] * W)
            set_moves(gx, gy, 0)

            result = max(result, max([max(row) for row in grid]))

print(result)
