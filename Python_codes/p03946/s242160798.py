n,t=map(int,input().split())
a=list(map(int,input().split()))
max=0
min=1000000000000000000000000000000000000
ans=1
for i in range(len(a)-1):
  if a[i]<min:
    min=a[i]
  elif min==a[i] or max==a[i]-min:
    ans+=1
  elif max<a[i]-min:
    ans=1
    max=a[i]-min
if a[len(a)-1]-min==max:
  ans+=1
print(ans)