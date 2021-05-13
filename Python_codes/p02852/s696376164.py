n,m=map(int,input().split())
s=list(input())
s.reverse()
now=0;l=[]
while True:
  tmp=now
  now+=m
  now=min(n,now)
  if now==n:
    l.append(str(now-tmp))
    break
  while s[now]=='1':
    now-=1
    if now==tmp:
      print(-1)
      exit()
  l.append(str(now-tmp))
l.reverse()
print(' '.join(l))