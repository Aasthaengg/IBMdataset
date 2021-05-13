#!/usr/bin/env python3

N,K = [int(i) for i in input().split()]

if N == 0 or N % K == 0:
    ans = 0
elif N > K:
    ans = N % K
    ans = min(ans, abs(ans - K))
else:
    ans = min(N, abs(N - K))
    ans = min(ans, abs(ans - K))

print(ans)
