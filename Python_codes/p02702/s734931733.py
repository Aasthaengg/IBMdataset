# https://atcoder.jp/contests/abc164/tasks/abc164_d

import sys
input = sys.stdin.readline


S = input().rstrip()

res = 0

x = 0
p = 1
MOD = 2019
reminder = [0]*2019
reminder[0] = 1
for s in reversed(S):
    """ 累積和 """
    x += int(s)*p
    x %= MOD
    p *= 10
    p %= MOD
    res += reminder[x]
    reminder[x] += 1

print(res)