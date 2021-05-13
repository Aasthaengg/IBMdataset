import collections

n=int(input())
g=[[] for _ in range(n+1)]
for _ in range(n-1):
  a,b=map(int,input().split())
  g[a].append(b)
  g[b].append(a)
c=list(map(int,input().split()))
c=sorted(c,reverse=True)
m=sum(c)-c[0]
ans=[0]*(n+1)
ans[1]=c[0]
q=collections.deque()
q.append(1)
checked=[0]*(n+1)
checked[1]=1
cnt=1
while len(q):
  tmp=q.popleft()
  for v in g[tmp]:
    if checked[v]==0:
      checked[v]=1
      q.append(v)
      ans[v]=c[cnt]
      cnt+=1
print(m)
print(*ans[1:])