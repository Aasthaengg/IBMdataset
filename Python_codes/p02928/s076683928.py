N, K = map(int, input().split())
A = list(map(int, input().split())) * 2
mod = 10**9 + 7
ans = 0
b = 0
c = 0

for i in range(N):
    for j in range(i + 1, 2 * N):
        if j == N:
            c = b
        if A[i] > A[j] and j < N:
            b += 1
        elif A[i] > A[j] and j >= N:
            c += 1
    
    if b == c - b:
        ans += b * K * (K + 1) // 2
    else:
        ans += b * K + (c - b) * K * (K - 1) // 2
    
    b = 0
    c = 0

print(ans % mod)