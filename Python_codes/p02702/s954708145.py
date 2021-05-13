# coding: utf-8
import sys

sr = lambda: sys.stdin.readline().rstrip()
ir = lambda: int(sr())
lr = lambda: list(map(int, sr().split()))

# modulo 2019 で同じもの、右からApple Pen
MOD = 2019
S = sr()
remain = [0] * 2019
remain[0] = 1
answer = 0
power = 1
cur = 0
for s in S[::-1]:
    num = int(s)
    cur += num * power
    cur %= MOD
    answer += remain[cur]
    remain[cur] += 1
    power *= 10; power %= MOD

print(answer)
