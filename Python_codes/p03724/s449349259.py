n,m=map(int,input().split())
d=dict()
for _ in range(m):
  a,b=map(int,input().split())
  if a not in d:
    d[a]=1
  else:
    d[a]+=1
  if b not in d:
    d[b]=1
  else:
    d[b]+=1
d=list(d.items())
for node,cnt in d:
  if cnt%2:
    print('NO')
    exit()
print('YES')