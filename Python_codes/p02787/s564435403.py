H, N = map(int, input().split())
A_list = []
B_list = []
for i in range(N):
    A, B = map(int, input().split())
    A_list.append(A)
    B_list.append(B)

dp = [[10**8+1]*(H) for _ in range(N+1)] # DPテーブルの作成

for i in range(N):
    for j in range(H):
        if j < A_list[i]: # 選ばない時
            #dp[i+1][j] = dp[i][j]
            dp[i+1][j] = min(dp[i][j],B_list[i])
        else: # 選ぶ時
            dp[i+1][j] = min(dp[i][j],dp[i+1][j-A_list[i]]+B_list[i])
        #print(i,j,dp[i+1]) #debug

#print(dp[N])
print(dp[N][H-1])