import sys
input=sys.stdin.readline
def main():
  n,k=map(int,input().split())
  a=list(map(int,input().split()))
  dp=[[-1]*(2) for i in range(51)]
  dp[0][0]=0
  maxdigit=50
  for i in range(maxdigit):
    mask=1<<(maxdigit-i-1)
    cnt=0
    for j in range(n):
      if mask&a[j]:
        cnt+=1
    cost0=mask*cnt
    cost1=mask*(n-cnt)
    if dp[i][1]!=-1:
      dp[i+1][1]=max(dp[i+1][1],dp[i][1]+max(cost0,cost1))
    if dp[i][0]!=-1:
      if k&mask:
        dp[i+1][0]=max(dp[i+1][0],dp[i][0]+cost1)
        dp[i+1][1]=max(dp[i+1][1],dp[i][0]+cost0)
      else:
        dp[i+1][0]=max(dp[i+1][0],dp[i][0]+cost0)
  return print(max(dp[maxdigit][0],dp[maxdigit][1]))
if __name__=='__main__':
  main()