N = int(input())
 
DP = [[0, 0, 0] for _ in range(N+1)]
 
for i in range(1, N+1):
    a, b, c = map(int, input().split())
    DP[i][0] = max(DP[i - 1][1] + a, DP[i - 1][2] + a)
    DP[i][1] = max(DP[i - 1][0] + b, DP[i - 1][2] + b)
    DP[i][2] = max(DP[i - 1][0] + c, DP[i - 1][1] + c)
 
 
print(max(DP[N]))