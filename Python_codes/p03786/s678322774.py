# https://atcoder.jp/contests/agc011/tasks/agc011_b

import sys
input = sys.stdin.buffer.readline

n = int(input())
A = sorted([int(i) for i in input().strip().split()])
_max = A[-1]
cul_sum = [0] * (n + 1)

for i in range(1, n + 1):
    cul_sum[i] = cul_sum[i - 1] + A[i - 1]

ptr = 0
for i in range(1, n + 1):
    if cul_sum[i] * 2 < A[i]:
        ptr = i
    elif cul_sum[i] * 2 >= _max:
        print(n - ptr)
        sys.exit()
