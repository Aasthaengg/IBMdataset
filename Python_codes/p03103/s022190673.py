n,m=map(int,input().split())
a=[list(map(int,input().split())) for _ in range(n)]
a.sort()
sm=0
c=0
for l in a:
  if l[1]<m-c:
    c+=l[1]
    sm+=l[1]*l[0]
  else:
    sm+=(m-c)*l[0]
    break
print(sm)