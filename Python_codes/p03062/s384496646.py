n = int(input())
A = list(map(int, input().split()))

DP = [[0, 0] for _ in range(n + 1)]
DP[0][1] = -1e20
# print(DP)
for i in range(n):
    for j in [0, 1]:
        DP[i + 1][0] = max(DP[i][0] + A[i], DP[i][1] - A[i])
        DP[i + 1][1] = max(DP[i][0] - A[i], DP[i][1] + A[i])

print(DP[-1][0])