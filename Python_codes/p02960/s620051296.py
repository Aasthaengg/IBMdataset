def main():
  s=list(input())
  n=len(s)
  dp=[0]*13
  mod=pow(10,9)+7
  if s[-1]=='?':
    dp=[1]*10+[0]*3
  else:
    dp[int(s[-1])]=1
  p_dp=[0]*13
  for i in range(2,n+1):
    if s[-i]=='?':
      for j in range(10):
        a=(j*pow(10,i-1,13))%13
        for k in range(13):
          p_dp[(a+k)%13]+=dp[k]
    else:
      j=int(s[-i])
      a=(j*pow(10,i-1,13))%13
      for k in range(13):
        p_dp[(a+k)%13]+=dp[k]
    
    for k in range(13):
      p_dp[k]%=mod
    dp=[k for k in p_dp]
    p_dp=[0]*13
  print(dp[5])

if __name__=='__main__':
  #import datetime
  #print(datetime.datetime.now())
  main()
  #print(datetime.datetime.now())
