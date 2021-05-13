# coding: utf-8
import sys
from collections import defaultdict

sr = lambda: sys.stdin.readline().rstrip()
ir = lambda: int(sr())
lr = lambda: list(map(int, sr().split()))

# 左から累積和のリストを持ちながらApplePen
N, M = lr()
A = lr()
dic = defaultdict(int)
dic[0] = 1
answer = 0
cur = 0
for a in A:
    cur += a
    cur %= M
    answer += dic[cur]
    dic[cur] += 1

print(answer)
