n=int(input())
edge=[[]for _ in range(n)]
for _ in range(n-1):
  a,b=map(int,input().split())
  a-=1
  b-=1
  edge[a].append(b)
  edge[b].append(a)
c=list(map(int,input().split()))
c.sort(reverse=1)
print(sum(c)-c[0])
d=[-1]*n
d[0]=c[0]
Q=[0]
visited={0}
ind=1
while Q:
  P=[]
  for i in Q:
    for j in edge[i]:
      if j in visited:continue
      visited.add(j)
      d[j]=c[ind]
      ind+=1
      P.append(j)
  Q=P
print(*d)