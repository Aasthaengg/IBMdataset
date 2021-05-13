N = int(input())
H = [float('inf')] + list(map(int, input().split()))
DP = [0] * (N+1)

for i in range(2, N+1):
    DP[i] = min(abs(H[i] - H[i-1]) + DP[i-1], abs(H[i] - H[i-2]) + DP[i-2])
print(DP[N])
