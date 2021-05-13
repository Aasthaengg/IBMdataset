import sys
input = sys.stdin.readline

def solve():  
  n,k = (int(i) for i in input().split())
  a = list(int(i) for i in input().split())
  digit = [0]*62
  for i in range(n):
    an = a[i]
    j = 0
    while an>0:
      digit[j] += an%2
      an //= 2
      j+=1
  digit = digit[::-1]


  dp = [[0]*2  for _ in range(63)]
  for i in range(62):
    value = 2**(62-i-1)
    temp = digit[i]

    if (dp[i][1]):
        dp[i+1][1] = max(dp[i+1][1],dp[i][1]+value*max(n-temp,temp))  
      
    if (k>>(62-i-1)&1):
      dp[i+1][1] = max(dp[i][0] +value*temp,dp[i+1][1])
      dp[i+1][0] = max(dp[i+1][0],dp[i][0]+ value*(n-temp))
    else: 
      dp[i+1][0] = max(dp[i+1][0],dp[i][0]+ value*temp)
      

  #print(dp)
  print(max(dp[-1][0],dp[-1][1]))
    
solve()