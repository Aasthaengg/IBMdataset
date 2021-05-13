n,x=map(int,input().split())
a=list(map(int,input().split()))
a.sort()
ans=0
for i in range(n-1):
  if a[i]>x:
    print(ans)
    exit()
  else:
    x-=a[i]
    ans+=1
if x==a[n-1]:
  print(n)
else:
  print(ans)