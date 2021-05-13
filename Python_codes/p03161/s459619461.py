n , k = map(int, input().split())
H = list(map(int, input().split()))

DP = [0 for i in range(n)]
DP[0] = 0
for i in range(1, n):
    DP[i] = DP[i - 1] + abs(H[i - 1] - H[i])
    for j in range(2, k+1):
        if i - j >= 0:
            tmp = DP[i - j] + abs(H[i - j] - H[i])
            DP[i] = min(DP[i], tmp)
        else:
            pass

print(DP[n - 1])