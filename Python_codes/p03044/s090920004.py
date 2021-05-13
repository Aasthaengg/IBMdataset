n=int(input())
l=[[] for i in range(n)]
ans=[-1 for i in range(n)]
for i in range(n-1):
  u,v,w=[int(x) for x in input().rstrip().split()]
  l[u-1].append([v-1,w])
  l[v-1].append([u-1,w])

def bfs():
  ans[0]=0
  que=[0]
  while(que):
    now=que.pop(0)
    for i,j in l[now]:
      if ans[i]==-1:
        if j%2==0:
          ans[i]=ans[now]
        else:
          ans[i]=(ans[now]+1)%2
        que.append(i)

bfs()
for i in ans:print(i)