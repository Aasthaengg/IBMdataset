n=int(input())
a=list(map(int,input().split()))
temp=sum(a)
temp1=a[0]
ans=abs(temp-temp1*2)
for i in range(1,n-1):
  temp1=temp1+a[i]
  ans=min(ans,abs(temp-temp1*2))
print(ans)