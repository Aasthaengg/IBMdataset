N, K = map(int,input().split())
ans = 0
for b in range(K+1, N+1):
    k = (N+1) // b
    temp = (b - K) * k + max(0, N - (K + b * k) + 1)
    if K == 0:
        temp -= 1
    ans += temp
print(ans)