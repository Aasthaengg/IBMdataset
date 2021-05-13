n = int(input())
ABC = []

for _ in range(n):
  ABC.append(list(map(int, input().split())))
  
dp = [[0]*3 for _ in range(n)]

for n_i in range(n):
  if n_i == 0:
    dp[n_i][0] = ABC[n_i][0]
    dp[n_i][1] = ABC[n_i][1]
    dp[n_i][2] = ABC[n_i][2]
  else:
    dp[n_i][0] = max(ABC[n_i][0]+dp[n_i-1][1], ABC[n_i][0]+dp[n_i-1][2])
    dp[n_i][1] = max(ABC[n_i][1]+dp[n_i-1][0], ABC[n_i][1]+dp[n_i-1][2])
    dp[n_i][2] = max(ABC[n_i][2]+dp[n_i-1][0], ABC[n_i][2]+dp[n_i-1][1])
    
print(max(dp[-1]))