import sys
sys.setrecursionlimit(2000)
n,q=map(int,input().split())
e=[[] for _ in range(n)]
cnt=[0]*n
for _ in range(n-1):
  a,b=map(int,input().split())
  e[a-1].append(b-1)
  e[b-1].append(a-1)
for _ in range(q):
  x,y=map(int,input().split())
  cnt[x-1]+=y
vis=[1]*n
queue=[0]
vis[0]=0
while queue:
  now=queue.pop()
  for i in e[now]:
    if vis[i]:
      queue.append(i)
      cnt[i]+=cnt[now]
      vis[i]=0
print(' '.join(map(str,cnt)))