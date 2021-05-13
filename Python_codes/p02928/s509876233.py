N, K = map(int, input().split())
A = list(map(int, input().split()))

mod = 10 ** 9 + 7

ai = 0
bi = 0

for i in range(N-1):
    for j in range(i+1, N):
        if(A[i] > A[j]):
            ai += 1
            ai %= mod

for i in range(N):
    for j in range(N):
        if (A[i] < A[j]):
            bi += 1
            bi %= mod

ansa = ai * K % mod
ansb = K * (K-1) // 2 % mod
ansb = ansb * bi % mod
ans = (ansa + ansb) % mod
print(ans)

