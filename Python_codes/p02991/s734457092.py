from collections import deque
n,m=map(int,input().split())
l=[[] for i in range(n+1)]
lb=[[] for i in range(n+1)]
d0={}#gから逆走して3の倍数回でいけるか
d1={}
d2={}
for i in range(n):
  d1[i+1],d2[i+1],d0[i+1]=0,0,0
for i in range(m):
  a,b=map(int,input().split())
  l[a].append(b)
  lb[b].append(a)
s,t=map(int,input().split())
q0=deque([t])
q1=deque([])
q2=deque([])
bool1=True
now=0
ans=-1
while q0 or q1 or q2:
  if now%3==0:
    while q0:
      a=q0.popleft()
      d=lb[a]
      for i in d:
        if d1[i]==1:
          pass
        else:
          d1[i]=1
          q1.append(i)
  elif now%3==1:
    while q1:
      a=q1.popleft()
      d=lb[a]
      for i in d:
        if d2[i]==1:
          pass
        else:
          d2[i]=1
          q2.append(i)
  elif now%3==2:
    while q2:
      a=q2.popleft()
      d=lb[a]
      for i in d:
        if i==s and bool1:
          ans=(now+1)//3
          bool1=False
        if d0[i]==1:
          pass
        else:
          d0[i]=1
          q0.append(i)
  now=now+1
print(ans)