# coding: utf-8
import sys
from bisect import bisect_left, bisect_right

sr = lambda: sys.stdin.readline().rstrip()
ir = lambda: int(sr())
lr = lambda: list(map(int, sr().split()))

N, K = lr()
X = lr()
if 0 in X:
    K -= 1

i = bisect_left(X, 0)
ne = X[:i]
i = bisect_right(X, 0)
po = X[i:]
INF = 10 ** 10
neg = [INF] * (K+1)  # 左からK本選ぶ場合、K-1本選ぶ場合・・・0本選ぶ場合
neg[-1] = 0
pos = [INF] * (K+1)
pos[0] = 0
for j in range(len(ne)):
    if -j-2 < -K-1:
        break
    neg[-j-2] = ne[-j-1]

for j in range(len(po)):
    if j+1 > K:
        break
    pos[j+1] = po[j]

answer = INF
for j in range(K+1):
    x = abs(neg[j]); y = abs(pos[j])
    mi = min(x, y)
    ma = max(x, y)
    temp = mi * 2 + ma
    if temp < answer:
        answer = temp
print(answer)
# 52