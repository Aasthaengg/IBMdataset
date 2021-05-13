h,w=map(int,input().split())
s=[]
s.append("#"*(w+2))
for i in range(h):
  s.append("#"+input()+"#")
s.append("#"*(w+2))
r=[[0]*(w+2) for i in range(h+2)]
l=[[0]*(w+2) for i in range(h+2)]
d=[[0]*(w+2) for i in range(h+2)]
u=[[0]*(w+2) for i in range(h+2)]

for i in range(1,h+1):
  for j in range(w+1,0,-1):
    if s[i][j]=="#":
      r[i][j]=0
    else:
      r[i][j]+=r[i][j+1]+1
# print(r)
for i in range(1,h+1):
  for j in range(1,w+1):
    if s[i][j]=="#":
      l[i][j]=0
    else:
      l[i][j]+=l[i][j-1]+1
# print(l)
for i in range(1,h+1):
  for j in range(1,w+1):
    if s[i][j]=="#":
      u[i][j]=0
    else:
      u[i][j]+=u[i-1][j]+1
# print(u)
for i in range(h+1,0,-1):
  for j in range(1,w+1):
    if s[i][j]=="#":
      d[i][j]=0
    else:
      d[i][j]+=d[i+1][j]+1
# print(d)
ans=0
for i in range(1,h+1):
  for j in range(1,w+1):
    ans=max(r[i][j]+l[i][j]+u[i][j]+d[i][j]-3,ans)
print(ans)