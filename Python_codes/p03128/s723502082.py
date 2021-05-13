n,m=map(int,input().split())
arr=list(map(int,input().split()))
arr=sorted(arr,reverse=True)
dic={1:2,2:5,3:5,4:4,5:5,6:6,7:3,8:7,9:6}
dp=[-1]*(n+1)
dp[0]=0
for i in range(n+1):
  for val in arr:
    if i-dic[val]<0:
      continue
    else:
      dp[i]=max(dp[i],dp[i-dic[val]]+1)
ans=''
tmp=n
while tmp>0:
  for val in arr:
    if tmp-dic[val]<0:
      continue
    if dp[tmp]==dp[tmp-dic[val]]+1 and dp[tmp-dic[val]]!=-1:
      ans+=str(val)
      tmp-=dic[val]
      break
print(ans)