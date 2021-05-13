#!/usr/bin/env python3
N = int(input())
K = int(input())
X = int(input())
Y = int(input())

x = min(N, K)
y = max(0, N - K)
ans = X * x + Y * y
print(ans)
