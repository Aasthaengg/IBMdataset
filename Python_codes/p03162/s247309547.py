def solve(arr,dp,N):
    dp[0][0],dp[0][1],dp[0][2]=matrix[0][0],matrix[0][1],matrix[0][2]
    for i in range(1,N):
        dp[i][0]=arr[i][0]+max(dp[i-1][1],dp[i-1][2])
        dp[i][1]=arr[i][1]+max(dp[i-1][0],dp[i-1][2])
        dp[i][2]=arr[i][2]+max(dp[i-1][0],dp[i-1][1])
    return max(dp[-1])
if __name__ == "__main__":
    N=int(input())
    matrix=[[0 for j in range(3)] for i in range(N)]
    dp=[[0 for j in range(3)] for i in range(N)]
    for i in range(N):
        matrix[i][0],matrix[i][1],matrix[i][2]=map(int,input().split())
    print(solve(matrix,dp,N))