# coding: utf-8
import sys
import numpy as np

sr = lambda: sys.stdin.readline().rstrip()
ir = lambda: int(sr())
lr = lambda: list(map(int, sr().split()))

N, C = lr()
XV = np.array([lr() for _ in range(N)])
right = XV[:, 1]
r_pos = XV[:, 0]
rcum = right.cumsum() - r_pos
r_max_cum = np.maximum.accumulate(rcum)
left = right[::-1]
l_pos = (C - r_pos)[::-1]
lcum = left.cumsum() - l_pos
l_max_cum = np.maximum.accumulate(lcum)

answer = max(0, r_max_cum[-1], l_max_cum[-1])
# i個目で折り返す
for i in range(N-1):
    temp = rcum[i] - r_pos[i]  # 帰りの距離を引く
    temp += l_max_cum[N-2-i]
    if temp > answer:
        answer = temp

for i in range(N-1):
    temp = lcum[i] - l_pos[i]  # 帰りの距離を引く
    temp += r_max_cum[N-2-i]
    if temp > answer:
        answer = temp

print(answer)
