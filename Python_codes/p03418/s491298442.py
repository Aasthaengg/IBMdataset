N, K = map(int, input().split())

if K == 0:
    print(N*N)
    exit()
ans = 0
for i in range(N - K):
    b = K + 1 + i
    n1 = N // b
    if n1 > 0:
        n2 = max(0, N % b - K + 1)
        ans += (i + 1) * n1 + n2
print(ans)
