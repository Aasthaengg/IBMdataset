import heapq as hp

n,q=[int(x) for x in input().rstrip().split()]
l=[[] for i in range(n)]
pul=[0]*n
for i in range(n-1):
  a,b=map(int,input().split())
  l[a-1].append(b-1)
  l[b-1].append(a-1)


for i in range(q):
  p,x=map(int,input().split())
  pul[p-1]+=x


ans=[0]*n
def dfs():
  val=0
  que=[[0,val]]
  done=[0]*n  

  while(que):
    now,val=que.pop()
    if done[now]==1:
      continue
    val+=pul[now]
    ans[now]=val
    done[now]=1

    for i in l[now]:
      if done[i]==0:
        que.append([i,val])

dfs()
print(*ans)
