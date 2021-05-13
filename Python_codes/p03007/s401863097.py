import sys
from bisect import bisect_left

sr = lambda: sys.stdin.readline().rstrip()
ir = lambda: int(sr())
lr = lambda: list(map(int, sr().split()))

N = ir()
A = lr()
A.sort()
# -の合計数は最大N-1、最小N//2
minus = bisect_left(A, 0)
# minusは負の数の個数
m = min(minus, N-1)
if m == 0: m += 1
# mは最終的にマイナスにする数
answer = -sum(A[:m]) + sum(A[m:])
print(answer)
cur = A[0]
for i in range(m, N-1):
    print(cur, A[i])
    cur -= A[i]

A[0] = cur
cur = A[N-1]
for i in range(m):
    print(cur, A[i])
    cur -= A[i]

# 53
