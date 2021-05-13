# coding:UTF-8
import sys
from math import factorial

MOD = 10 ** 9 + 7
INF = float('inf')

N = int(input())    # 数字
A = list(map(int, input().split()))     # スペース区切り連続数字

mny = 1000
m = A[0]
for i in range(1, N):
    if A[i] < m:
        m = A[i]
    if A[i] > m:
        if i == N-1:
            num = mny // m
            mny += num * (A[i] - m)
        elif A[i+1] <= A[i]:
            num = mny // m
            mny += num * (A[i] - m)
            m = A[i+1]

print("{}".format(mny))
