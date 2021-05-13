n,m=map(int,input().split())
lst=[[] for i in range(n)]
cnt=[]
ans=m

for i in range(m):
  a,b=map(int,input().split())
  lst[a-1].append(b-1)
  lst[b-1].append(a-1)
  cnt.append([a-1,b-1])


for i in cnt:
  judge=False
  j=i[0]
  Q=[j]
  visited=[False]*n
  
  while Q:
      v=Q.pop(0)
      for k in lst[v]:
        if (v==i[0] and k==i[1]) or (v==i[1] and k==i[0]):
          continue
        if visited[k]==False:
              visited[k]=True
              Q.append(k)

  if visited[i[1]]==True:
      judge=True

  
  if judge:
    ans-=1


print(ans)