result = 0
N, K = list(map(int , input().split()))
for b in range(K + 1, N + 1):
    result += (N // b) * (b - K) + max(N - (N // b) * b - max(K - 1, 0), 0)
print(result)