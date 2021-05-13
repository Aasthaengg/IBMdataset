'''
Created on 2020/09/14

@author: harurun
'''
def main():
  import sys
  pin=sys.stdin.readline
  pout=sys.stdout.write
  perr=sys.stderr.write

  S=int(pin())
  mod=10**9+7
  dp=[0]*(S+1)
  dp[0]=1
  for i in range(3,S+1):
    dp[i]=(dp[i-1]+dp[i-3])%mod 
  print(dp[S])
  return
main()
#解説AC