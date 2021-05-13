n=int(input())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
x=sum(b)
for i in range(n):
  s=a[i]+a[i+1]
  t=b[i]
  x-=max(0,t-s)
  a[i+1]-=max(0,b[i]-a[i])
  a[i+1]=max(a[i+1],0)
print(x)