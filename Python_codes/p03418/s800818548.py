N, K = map(int, input().split())

if K == 0:
    print(N**2)
    exit()

ans = 0
for i in range(K+1, N+1):
    if N % i < K:
        temp = 0
    else:
        temp = N % i - K + 1

    ans += N // i * (i - K) + temp

print(ans)