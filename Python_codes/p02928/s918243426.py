#coding: utf-8
N, K = map(int, input().split())
A = list(map(int, input().split()))
ans = 0
mod = 10**9 + 7
jun = [0 for _ in range(N)]
inv = [0 for _ in range(N)]
for i in range(N):
    for j in range(N):
        if j < i:
            if A[i] < A[j]:
                jun[i] += 1
        else:
            if A[i] < A[j]:
                inv[i] += 1
for i in range(N):
    ans += K * (jun[i] * (K+1) + inv[i] * (K-1)) // 2
    ans %= mod

print(ans)