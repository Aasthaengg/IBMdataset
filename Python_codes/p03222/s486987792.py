h,w,k=map(int,input().split())
mod=10**9+7
dp=[[0]*w for _ in range(h+1)]
dp[0][0]=1
for i in range(1,h+1):
  for j in range(2**(w-1)):
    tmp=format(j,'b')
    if len(tmp)!=w-1:
      tmp=(w-1-len(tmp))*'0'+tmp
    flag=True
    for l in range(1,w-1):
      if tmp[l]=='1' and tmp[l-1]=='1':
        flag=False
        break
    if flag==False:
      continue
    else:
      arr=[i for i in range(1,w+1)]
      for m in range(w-1):
        if tmp[m]=='1':
          arr[m],arr[m+1]=arr[m+1],arr[m]
      for m in range(w):
        dp[i][m]+=dp[i-1][arr[m]-1]%mod
print(dp[h][k-1]%mod)