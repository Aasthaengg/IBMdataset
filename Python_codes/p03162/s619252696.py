n = int(input())

all_days = []
for _ in range(n):
  day = input()
  day = day.split()
  for i in range(len(day)):
    day[i] = int(day[i])
  all_days.append(day)
  
def vacation(arr):
    dp = [[0,1,2] for i in range(len(arr))]
    dp[0][0] = arr[0][0]
    dp[0][1] = arr[0][1]
    dp[0][2] = arr[0][2]
    
    for i in range(1, len(arr)):
        dp[i][0] = arr[i][0] + max(dp[i-1][1], dp[i-1][2])
        dp[i][1] = arr[i][1] + max(dp[i-1][0], dp[i-1][2])
        dp[i][2] = arr[i][2] + max(dp[i-1][1], dp[i-1][0])
    
    return max(max(dp[-1][0], dp[-1][1]), dp[-1][2])
  
print(vacation(all_days))