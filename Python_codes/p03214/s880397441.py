n=int(input())
a=list(map(int,input().split()))
ave=sum(a)/n
x=100
ans=-1
for i in range(n):
  if x>abs(ave-a[i]):
    x=abs(ave-a[i])
    ans=i
print(ans)