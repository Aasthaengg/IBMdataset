N, K = map(int, input().split())
abs_g = [(i, j) for i in range(1, N) for j in range(i + 1, N + 1)][::-1]

if len(abs_g) - (N - 1) < K:
    print(-1)
    exit()

print(len(abs_g) - K)
[print(i, j) for i, j in abs_g[K:]]
