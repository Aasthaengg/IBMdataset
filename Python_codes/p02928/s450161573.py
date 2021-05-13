N, K = map(int, input().split())
A = list(map(int, input().split()))
mod = 10**9+7
counter1 = [0] * N
counter2 = [0] * N
for i in range(N):
    p, q = 0, 0
    for j in range(i+1, N):
        if A[i] > A[j]:
            counter1[i] += 1
    
    for j in range(N):
        if A[i] > A[j]:
            counter2[i] += 1

ans = 0
for i in range(N):
    c1 = counter1[i]
    c2 = counter2[i]
    ans = (ans + (c1 * K + c2 * K * (K - 1) // 2)) % mod
print(ans)