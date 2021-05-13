#  入力
N = int(input())
A = [int(x) for x in input().split()]

# 初期化
dp = [[0] * (N+1) for _ in range(N+1)]
dp[0][0] = 0

for i in range(0,N):

    # 最も嬉しさの高い子供から場所を選択していく
    a = max(A)
    id = A.index(a)
    
    for x in range(0,i+1):
        y = i - x

        d = dp[x][y]
        tmp = d + a * (id - x)
        if dp[x+1][y] < tmp:
        	dp[x+1][y] = tmp
        tmp = d + a * (((N-1)-y) - id)            
        if dp[x][y+1] < tmp:
        	dp[x][y+1] = tmp
        
    A[id] = 0

ans = 0
for i in range(N+1):
    ans = max(ans, dp[i][N-i])
print(ans)