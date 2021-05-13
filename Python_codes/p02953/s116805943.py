n=int(input())
h=list(map(int,input().split()))
res=h[n-1]
for i in range(1,n):
  if h[n-1-i]<=res:
    res=h[n-1-i]
  elif h[n-1-i]==res+1:
    res=h[n-1-i]-1
  else:
    print('No')
    exit()
print('Yes')