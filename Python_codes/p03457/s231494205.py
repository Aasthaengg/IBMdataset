# -*- coding: utf-8 -*-
n = int(input())
t_now = 0
pos = [0,0]
l = [list(map(int, input().split())) for _ in range(n)]

for t, x, y in l:
    t_d = t - t_now
    range_move = list(range(-t_d, t_d+1, 2))

    pos_d = (x-pos[0]) + (y-pos[1])

    if pos_d in range_move:
        t_now = t
        pos = [x, y]
    else:
        print('No')
        exit()

print('Yes')
