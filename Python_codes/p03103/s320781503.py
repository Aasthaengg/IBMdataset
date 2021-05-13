n,m=map(int,input().split())
t=[0]*n
ans=0
temp=0
for i in range(n):
  at,bt=map(int,input().split())
  t[i]=[at,bt]
t.sort()
i=0
while True:
  if temp+t[i][1]>=m:
    ans=ans+t[i][0]*(m-temp)
    break
  else:
    ans=ans+t[i][0]*t[i][1]
    temp=temp+t[i][1]
    i=i+1
print(ans)