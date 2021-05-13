N,C=map(int,input().split())
xv=[list(map(int,input().split())) for _ in range(N)]

l=[0]*N
l[0]=xv[0][1]
for i in range(1,N):
  l[i]=l[i-1]+xv[i][1]
for i in range(N):
  l[i]-=xv[i][0]

r=[0]*N
r[0]=xv[N-1][1]
for i in reversed(range(N-1)):
  r[N-1-i]=r[N-1-i-1]+xv[i][1]
for i in reversed(range(N)):
  r[N-1-i]-=C-xv[i][0]
  
ans=max(max(l),max(r))

lm=[0]*N
lm[0]=l[0]
for i in range(1,N):
  lm[i]=max(lm[i-1],l[i])
  
rm=[0]*N
rm[0]=r[0]
for i in range(1,N):
  rm[i]=max(rm[i-1],r[i])

for i in range(N-1):
  ans=max(ans,l[i]-xv[i][0]+rm[N-1-i-1])
for i in range(N-1):
  ans=max(ans,r[i]-C+xv[N-1-i][0]+lm[N-1-i-1])
  
print(max(ans,0))

