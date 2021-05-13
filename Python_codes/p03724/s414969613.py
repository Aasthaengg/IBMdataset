from collections import Counter
N,M=map(int,input().split())
a=[0]*M
b=[0]*M
c=[]
for i in range(M):
  a[i],b[i]= map(int,input().split())
  c.append(a[i])
  c.append(b[i])
  
d=dict(Counter(c))
ans="YES"
for e in d:
  if d[e]%2==1:
    ans="NO"
print(ans)