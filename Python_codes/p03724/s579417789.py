n,m=map(int,input().split())
x=[0]*n
for i in range(m):
  a,b=map(int,input().split())
  x[a-1]+=1
  x[b-1]+=1
ans="YES"
for i in range(n):
  if x[i]%2:ans="NO"
print(ans)