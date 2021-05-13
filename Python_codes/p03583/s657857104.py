# https://atcoder.jp/contests/tenka1-2017/tasks/tenka1_2017_c
# 式をこねくり回せ

N = int(input())

from itertools import product

for n, h in product(range(1, 3501), range(1, 3501)):
    bunbo = (4 * n * h - N * n - N * h)
    if bunbo <= 0:
        continue
    w = (N * h * n) / bunbo
    if w.is_integer():
        print(n, h, int(w))
        exit()
