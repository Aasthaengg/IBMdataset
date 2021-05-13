N, K = map(int, input().split())
A = list(map(int, input().split()))

mod = 10**9+7
res = 0

for i in range(N):
    for j in range(i):
        if A[j] < A[i]:
            res += (K-1)*K//2
            res %= mod
    for j in range(i+1, N):
        if A[j] < A[i]:
            res += (K+1)*K//2
            res %= mod

print(res)