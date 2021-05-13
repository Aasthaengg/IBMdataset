# coding: utf-8
N = int(input())
K = int(input())
x = int(input())
y = int(input())

ans = min(N, K) * x + max((N-K), 0) * y
print(ans)