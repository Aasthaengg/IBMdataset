


def findmin(arr,n):
  dp = [0]*n
  dp[1] = abs(arr[0]-arr[1])
  for i in range(2,n):
    dp[i] = min(dp[i-1]+abs(arr[i-1]-arr[i]), dp[i-2]+abs(arr[i-2]-arr[i]))
  return dp[-1]

n = int(input())
arr = list(map(int,input().split()))
print(findmin(arr,n))