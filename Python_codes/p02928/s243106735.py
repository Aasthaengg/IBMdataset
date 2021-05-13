N, K = map(int, input().split())
A = list(map(int, input().split()))
MOD = 10**9+7

p, q = [0]*N, [0]*N
for i in range(N):
    for j in range(i):
        if A[i] > A[j]:
            p[i] += 1
            q[i] += 1
    for j in range(i+1,N):
        if A[i] > A[j]:
            p[i] += 1

ans = 0
if K % 2 == 0:
    k = ((K//2)*(K+1)) % MOD
else:
    k = (K*((K+1)//2)) % MOD
for i in range(N):
    ans = (ans + (((k * p[i]) % MOD - (K*q[i]) % MOD) % MOD)) % MOD
print(ans)