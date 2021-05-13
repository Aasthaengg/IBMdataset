n = int(input())
h = [] #happiness
for i in range(n):
 a_input, b_input, c_input = map(int, input().split())
 h.append([a_input, b_input, c_input]) 
dp = [[0 for _ in range(3)] for _ in range(n+1)]
for i in range(1, n+1):
 for j in range(3):
   for k in range(3):
     if j != k and dp[i][j] < dp[i-1][k] + h[i-1][j]:
       dp[i][j] = dp[i-1][k] + h[i-1][j]
ans = 0
for j in range(3):
 if ans < dp[n][j]:
   ans = dp[n][j]
print(ans)