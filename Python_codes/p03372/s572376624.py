import sys
from itertools import accumulate
import bisect
n, c = [int(i) for i in sys.stdin.readline().split()]
x_ls = []
inv_x_ls = []
v_ls = []
for i in range(n):
    x, v = [int(i) for i in sys.stdin.readline().split()]
    x_ls.append(x)
    inv_x_ls.append(c - x)
    v_ls.append(v)
inv_v_ls = v_ls[::-1]
inv_x_ls = inv_x_ls[::-1]
v_ls = [0] + [v - x for v, x in zip(accumulate(v_ls), x_ls)]
inv_v_ls = [0] + [v - x for v, x in zip(accumulate(inv_v_ls), inv_x_ls)]
x_ls = [0] + x_ls
inv_x_ls = [0] + inv_x_ls
best_v = 0
best_inv_v = 0
for i in range(n + 1):
    best_v = max(best_v, v_ls[i])
    best_inv_v = max(best_inv_v, inv_v_ls[i])
    v_ls[i] = best_v
    inv_v_ls[i] = best_inv_v

best = 0
for tokei in range(n+1):
    tokei_dis = x_ls[tokei]
    hantokei = max(0, inv_v_ls[n - tokei] - tokei_dis)
    res = v_ls[tokei] + hantokei
    best = max(best, res)
for hantokei in range(n+1):
    hantokei_dis = inv_x_ls[hantokei]
    tokei = max(0, v_ls[n - hantokei] - hantokei_dis)
    res = inv_v_ls[hantokei] + tokei
    best = max(best, res)
print(best)