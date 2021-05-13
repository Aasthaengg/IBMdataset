n,c=map(int,input().split())
g=[[0]*3 for i in range(n)]
for i in range(n):
  g[i]=list(map(int,input().split()))
g.sort(key=lambda x: x[0])
g.sort(key=lambda x: x[2])
T=[0]*(10**5+3)
i=0
while i<n:
  if i!=n-1 and g[i][2]==g[i+1][2] and g[i][1]==g[i+1][0]:
    T[g[i][0]]+=1
    i=i+1
    T[g[i][1]]-=1
    i=i+1
  else:
    T[g[i][0]]+=1
    T[g[i][1]+1]-=1
    i=i+1
ans=0
a=0
for i in range(len(T)):
  a=a+T[i]
  if a>ans:
    ans=a
print(ans)