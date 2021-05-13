#!/usr/bin/env python3
import sys
from itertools import accumulate
from bisect import bisect_left

N, M = [int(_) for _ in input().split()]
A = [int(_) for _ in input().split()]

A2 = sorted(A, reverse=True)
A = sorted(A)


# 必要となる左右合計の下限値 X を求める

def f1(m):
    cnt = 0
    for a1 in A2:
        tmp = bisect_left(A, m - a1)
        if tmp == N: break
        cnt += N - tmp

    return cnt >= M


l = 0
r = A2[0] * 2 + 10

while r - l > 1:
    m = (l + r) // 2
    if f1(m):
        l = m
    else:
        r = m

X = l
# print('X', X)

acc = list(accumulate(A2))  # 累積和

total_cnt = 0
ans = 0
for a in A2:
    # a を左手としたときの右手の最小値
    min_right = X - a
    if min_right > A[-1]:
        continue

    # 右手の値から出す手数を算出
    idx = bisect_left(A, min_right)
    cnt = N - idx

    # それらの全合計を加算
    ans += a * cnt + acc[cnt - 1]
    total_cnt += cnt

    # if total_cnt >= M:
    #     break
# total_cnt が大きすぎる場合は, その分だけ Xを減算. X は必要な両手合計の最小値なので, 減算すべきは必ず X*出しすぎた分 となる
if total_cnt > M:
    ans -= X * (total_cnt - M)
print(ans)
