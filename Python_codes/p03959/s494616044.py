n=int(input())
t=list(map(int,input().split()))
a=list(map(int,input().split()))
mod=pow(10,9)+7
ans=[[0,0] for _ in range(n)]
pre=0
for i in range(n):
  if t[i]>pre:
    ans[i]=[t[i],1]
  else:
    ans[i]=[t[i],0]
  pre=t[i]
#print(ans)
pre=0
for i in range(n-1,-1,-1):
  if a[i]>pre:
    if ans[i][1]==0 and ans[i][0]<a[i]:
      print(0)
      exit()
    elif ans[i][1]==1 and ans[i][0]!=a[i]:
      print(0)
      exit()
    else:
      ans[i]=[a[i],1]
  else:
    if ans[i][1]==0:
      ans[i][0]=min(ans[i][0],a[i])
    elif ans[i][1]==1 and ans[i][0]>a[i]:
      print(0)
      exit()
  pre=a[i]
b=1
for x,y in ans:
  if y==1:continue
  b*=x
  b%=mod
print(b)