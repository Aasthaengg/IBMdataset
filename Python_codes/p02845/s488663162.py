def main():
  n=int(input())
  a=list(map(int,input().split()))
  mod=pow(10,9)+7
  dp=[0,0,0] # dp[j]:前から順番に見た時の帽子jの数
  ans=1
  for ai in a:
    if ai in dp:
      ans*=dp.count(ai)
      ans%=mod
      dp[dp.index(ai)]+=1
    else:
      print(0)
      exit()
  print(ans)
if __name__=='__main__':
  main()
