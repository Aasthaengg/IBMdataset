N, K = map(int, input().split())
H = [float('inf')] + list(map(int, input().split()))
DP = [float('inf')] * (N+1)
DP[0] = 0
DP[1] = 0

for i, h in enumerate(H[1:], 1):
    for k in range(1, K+1):
        if i + k > N:
            break
        DP[i + k] = min(DP[i+k], DP[i] + abs(H[i + k] - h))
print(DP[N])


