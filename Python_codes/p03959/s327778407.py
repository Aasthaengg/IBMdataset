n=int(input())
t=list(map(int,input().split()))
a=list(map(int,input().split()))
if t[0]>a[0] or t[-1]<a[-1]:print(0);exit()
x=[1]*n
x[0]=x[-1]=0
for i in range(1,n):
  if t[i-1]!=t[i]:
    x[i]=0
    if t[i]>a[i]:print(0);exit()
for i in range(n-2,-1,-1):
  if a[i+1]!=a[i]:
    x[i]=0
    if t[i]<a[i]:print(0);exit()
ans=1
for i in range(n):
  if x[i]:
    ans*=min(t[i],a[i])
    ans%=10**9+7
print(ans)