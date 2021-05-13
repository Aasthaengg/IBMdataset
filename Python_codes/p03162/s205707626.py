def main():
  n=int(input())
  dp=[[0,0,0]]
  for i in range(1,n+1):
    a,b,c=map(int,input().split())
    dp.append([max(dp[i-1][1],dp[i-1][2])+a,max(dp[i-1][0],dp[i-1][2])+b,max(dp[i-1][0],dp[i-1][1])+c])
    #print(dp)
  print(max(dp[n]))
if __name__=='__main__':
  main()