import sys
import bisect
input = sys.stdin.buffer.readline


n = int(input())
A = sorted([int(i) for i in input().split()])
B = sorted([int(i) for i in input().split()])
C = sorted([int(i) for i in input().split()])

A_B = [0] * n
B_C = [0] * n
ans = 0

# A-B
for idx, a in enumerate(A):
    A_B[idx] = bisect.bisect_right(B, a)
# B-C
for idx, b in enumerate(B):
    B_C[idx] = n - bisect.bisect_right(C, b)

cul_sum = [0] * (n + 1)

for i in range(1, n + 1):
    cul_sum[i] = cul_sum[i - 1] + B_C[i - 1]


for idx in A_B:
    ans += cul_sum[n] - cul_sum[idx]

print(ans)
