n,m=map(int,input().split())
a=list(map(int,input().split()))
D=[2,5,5,4,5,6,3,7,6]
dp=[]
dp.append([0,0,0,0,0,0,0,0,0,0])
for i in range(n):
  dp.append([-1,-1,-1,-1,-1,-1,-1,-1,-1,-1])
allowed=[]
for i in a:
  allowed.append([i,D[i-1]])
for i in range(n):
  for j in allowed:
    temp=i+j[1]
    if temp<n+1 and dp[i][0]!=-1:
      if dp[temp][9]<dp[i][9]+1:
        for k in range(10):
          dp[temp][k]=dp[i][k]
        dp[temp][9]+=1
        dp[temp][j[0]-1]+=1
      elif dp[temp][9]==dp[i][9]+1:
        change=0
        for k in range(8,-1,-1):
          if k!=j[0]-1:
            breakflag=0
            if dp[temp][k]>dp[i][k]:
              change=-1
              breakflag=1
            if dp[temp][k]<dp[i][k]:
              change=1
              breakflag=1
          else:
            breakflag=0
            if dp[temp][k]>dp[i][k]+1:
              change=-1
              breakflag=1
            if dp[temp][k]<dp[i][k]+1:
              change=1
              breakflag=1
          if breakflag==1:
            break
        if change==1:
          for k in range(10):
            dp[temp][k]=dp[i][k]
          dp[temp][9]+=1
          dp[temp][j[0]-1]+=1
ans=[]
for i in range(8,-1,-1):
  for j in range(dp[n][i]):
    ans.append(str(i+1))
print(''.join(ans))