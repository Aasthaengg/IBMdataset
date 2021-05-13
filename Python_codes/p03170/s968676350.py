def main():
  n,k=map(int,input().split())
  num=[int(i) for i in input().split()]
  
  dp=[0]*(k+1)
  for i in range(k):
    flag=False
    for j in range(n):
      if i+1-num[j]>=0:
        if  dp[i+1-num[j]]==0:
          flag=True
          break
    if flag:
      dp[i+1]=1
    else:
      continue
  if dp[k]:
    print('First')
  else:
    print('Second')          
if __name__=='__main__':
  main()