n,m=map(int,input().split())
lst=[[] for i in range(n)]
visited=[False for i in range(n)]
ans=[0]*n

for i in range(m):
      a,b=map(int,input().split())
      lst[a-1].append(b-1)
      lst[b-1].append(a-1)

Q=[0]
visited[0]=True

while Q:
  v=Q.pop(0)
  for i in lst[v]:
        if visited[i]==False:
              visited[i]=True
              ans[i]=v
              Q.append(i)

print('Yes')

for i in range(1,n):
      print(ans[i]+1)