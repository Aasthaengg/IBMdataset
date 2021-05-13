import collections
q=collections.deque()
n,m=map(int,input().split())
for i in range(n):
  a,b=input().split()
  b=int(b)
  q.append([a,b])
t=0
while len(q)!=0:
  n=q.popleft()
  if n[1]<=m:
    t+=n[1]
    print(n[0],str(t))
  else:
    t+=m
    n[1]-=m
    q.append(n)
