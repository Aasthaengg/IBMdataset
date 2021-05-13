N, K = map(int, input().split())

if K == 0:
    print(N ** 2)
    exit()

ans = 0
for b in range(K + 1, N + 1):
    val1 = N // b * (b - K)
    if N % b == 0:
        val2 = 0
    else:
        val2 = max(0, N - (N // b) * b - K + 1)
    ans += val1 + val2
print(ans)
