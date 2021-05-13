n,q=[int(x) for x in input().rstrip().split()]
l=[[] for i in range(n)]
ans=[0]*n

for i in range(n-1):
  a,b=map(int,input().split())
  l[a-1].append(b-1)
  l[b-1].append(a-1)

for i in range(q):
  p,x=map(int,input().split())
  ans[p-1]+=x

def dfs():
  que=[0]
  done=[0]*n  
  done[0]=1
  while(que):
    now=que.pop()

    for i in l[now]:
      if done[i]==0:
        done[i]=1
        que.append(i)
        ans[i]+=ans[now]

dfs()
print(*ans)
