from collections import deque
n,m=map(int,input().split())
data=[[] for i in range(n+1)]
for i in range(m):
  a,b=map(int,input().split())
  data[a].append(b)
  data[b].append(a)
flag=[0]*(n+1)
cnt=-1
for i in range(1,n+1):
  if flag[i]==0:
    flag[i]=1
    que=deque([i])
    while que:
      h=que.popleft()
      for u in data[h]:
        if flag[u]==0:
          flag[u]=1
          que.append(u)
    cnt+=1
print(cnt)