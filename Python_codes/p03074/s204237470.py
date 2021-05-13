# coding: utf-8
import sys
import itertools

sr = lambda: sys.stdin.readline().rstrip()
ir = lambda: int(sr())
lr = lambda: list(map(int, sr().split()))

# 0か1の連続している人数のリスト、累積和
streak = [0, 0]
N, K = lr()
S = sr() + '2'
cur = 1
for i in range(N):
    if S[i] != S[i+1]:
        streak.append(cur)
        cur = 1
    else:
        cur += 1

streak_cum = list(itertools.accumulate(streak))
streak_cum.extend([streak_cum[-1], streak_cum[-1]])
if S[0] == '0':
    start = 0
else:
    start = 1
answer = 0

limit = len(streak_cum) - 1
for i in range(start, len(streak_cum), 2):
    result = streak_cum[min(limit, i+2*K+1)] - streak_cum[i]
    if result > answer:
        answer = result

print(answer)
# 52