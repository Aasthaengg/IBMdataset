n=int(input())
a=[int(input())for _ in range(n)]
if a[0]!=0:print(-1);exit()
for i in range(1,n):
  if a[i-1]+1<a[i]:print(-1);exit()
ans=0
for i in range(n-1,0,-1):
  if a[i]<=a[i-1]:ans+=a[i]
  else:ans+=1
print(ans)