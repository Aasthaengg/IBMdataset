n=int(input())
b=list(map(int,input().split()))

a=[0]*n
if n>2:
  
  for x in range(1,n-1):
    c=min(b[x-1],b[x])
    a[x]+=c
  
  a[0]+=b[0]
  a[n-1]+=b[n-2]

  ans=0

  for y in range(len(a)):
    ans+=a[y]
  print(ans)

else:
  print(b[0]*2)