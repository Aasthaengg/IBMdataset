n=int(input())
x=[0]*(n+1)
a=[int(input()) for _ in range(n)]
if a[0]!=0:
  print(-1)
  exit()
for i in range(1,n):
  if a[i]-a[i-1]>1:
    print(-1)
    exit()
res=0
for i in range(1,n):
  if a[i]==a[i-1]+1:
    res+=1
  else:
    res+=a[i]
print(res)