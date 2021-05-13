n,q=map(int,input().split())
lst=[[] for i in range(n)]
ans=[0]*n

for i in range(n-1):
      a,b=map(int,input().split())
      lst[a-1].append(b-1)
      lst[b-1].append(a-1)

for i in range(q):
    s,t=map(int,input().split())
    ans[s-1]+=t

Q=[0]

flag=[True]+[False]*(n-1)


while Q:
  v=Q.pop()
  flag[v]=True
  for i in lst[v]:
    if flag[i]:
      continue
    flag[i]=True
    ans[i]+=ans[v]
    Q.append(i)


print(' '.join([str(i) for i in ans]))