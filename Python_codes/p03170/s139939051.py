def main():
    n,k=map(int,input().split())
    a=list(map(int,input().split()))
    dp=[False]*(k+1)
    for j in range(1,k+1):
      for i in a:
        if 0<=j-i and dp[j-i]==False:
          dp[j]=True
    if dp[k]:
      print('First')
    else:
      print('Second')
main()