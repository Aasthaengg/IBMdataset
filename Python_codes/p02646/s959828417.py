import numpy as np
a, v = list(map(int, input().split(' ')))
b, w = list(map(int, input().split(' ')))
t = int(input())

if w >= v:
    print('NO')
    exit()

catchup_speed = (v - w)
start_dis = np.abs(b - a)

max_dis = t*catchup_speed

if start_dis <= max_dis:
    print('YES')
    exit()

print('NO')