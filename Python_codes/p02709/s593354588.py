#python3ではTLE
#input
N = int(input())
A = list(map(int, input().split()))

#output
B = [(i, a) for i, a in enumerate(A)]
B = sorted(B, key = lambda x:x[1], reverse = True)

dp = [[0] * (N+1) for i in range(N+1)]
#dp[i, j]を左i, 右jまで場所が決まった状態の最大値とする。
#i+j = Nとなる場合の最大値が答えとなる。

answer = 0
for i in range(N):
    dp[i+1][0] = dp[i][0] + B[i][1]*(abs(B[i][0]-i))
    for j in range(N):
        dp[0][j+1] = dp[0][j] + B[j][1]*(abs(N-1-B[j][0]-j))
        if i+j+1 < N:
            dp[i+1][j+1] = max(dp[i][j+1]+B[i+j+1][1]*(abs(B[i+j+1][0]-i)), dp[i+1][j] + B[i+j+1][1]*(abs(N-1-B[i+j+1][0]-j)))
    answer = max(answer, dp[i][N-i])

print(answer)