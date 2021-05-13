N, A, B = list(map(int, input().split()))
X = list(map(int, input().split()))

DP = [0] * N

for i in range(1, N):
    DP[i] = min((X[i] - X[i-1]) * A, B) + DP[i-1]

print(DP[N-1])
