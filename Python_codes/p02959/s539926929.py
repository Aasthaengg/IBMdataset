n=int(input())
a=[int(x) for x in input().rstrip().split()]
b=[int(x) for x in input().rstrip().split()]
ans=0
for i in range(len(b)):
  if a[i]+a[i+1]<=b[i]:
    ans+=a[i]+a[i+1]
    a[i]=0
    a[i+1]=0
  
  elif a[i]<=b[i]:
    ans+=a[i]
    ans+=(b[i]-a[i])
    a[i+1]=a[i+1]-(b[i]-a[i])
  else:
    a[i]-=b[i]
    ans+=b[i]
print(ans)