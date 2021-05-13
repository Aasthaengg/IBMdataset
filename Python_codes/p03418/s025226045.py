N, K = map(int, input().split())
print(sum((b - K) * (N // b) + max(0, N % b - K + 1) for b in range(K + 1, N + 1)) if K else N ** 2)
