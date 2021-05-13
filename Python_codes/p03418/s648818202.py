N, K = map(int, input().split())

cnt = 0
for b in range(K + 1, N + 1):
    x, y = divmod(N, b)

    k = b - K
    cnt += k * x - (K == 0) + max(0, y - (K - 1))

print(cnt)
