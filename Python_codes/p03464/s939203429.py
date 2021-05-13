k = int(input())
A = list(map(int,input().split()))[::-1]

dp = [[0,0] for _ in range(k+1)]
dp[0] = [2,2]

for i in range(k):
    dp[i+1][0] = ((dp[i][0]-1)//A[i] + 1)*A[i]
    dp[i+1][1] = (dp[i][1]//A[i])*A[i] + A[i] -1
    if dp[i+1][0] > dp[i+1][1]:
        print(-1)
        exit(0)
print(' '.join(str(i) for i in dp[k]))
