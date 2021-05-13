# coding: utf-8
import sys

sr = lambda: sys.stdin.readline().rstrip()
ir = lambda: int(sr())
lr = lambda: list(map(int, sr().split()))

# 桁DP, Lを超えないものと保留のもの
MOD = 10 ** 9 + 7
L = sr()
dp_dec = 1 # decide
dp_res = 2 # reserve
length = len(L)
for i in range(1, length):
    x, y = dp_dec, dp_res
    if L[i] == '1':
        dp_dec = x * 3 + y
        dp_res = y * 2
    else:
        dp_dec = x * 3
        dp_res = y
    dp_dec %= MOD
    dp_res %= MOD

answer = dp_dec + dp_res
print(answer % MOD)
