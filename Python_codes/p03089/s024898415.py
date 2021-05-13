n=int(input())
b=list(map(int,input().split()))
ans=[0]*n
t=0
while t<n:
  res=t
  for i in range(n-t):
    if b[n-t-1-i]==n-t-i:
      ans[t]=b[n-t-1-i]
      b.remove(b[n-t-1-i])
      t+=1
      break
  if t==res:
    print(-1)
    exit()
for i in range(n):
  print(ans[n-1-i])