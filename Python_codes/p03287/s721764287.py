from collections import defaultdict
import sys
input = sys.stdin.readline

N, M = [int(x) for x in input().split()]
A = [0] + [int(x) % M for x in input().split()]

# 累積和(mod M)に変える
for i in range(1, N + 1):
    A[i] += A[i - 1]
    A[i] %= M

candy = defaultdict(int) # default value is 0
for i in range(N + 1):
    candy[A[i]] += 1

ans = 0
for n in candy.values():
    ans += n * (n - 1) // 2

print(ans)