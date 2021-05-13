a,b=map(int,input().split())
c=list(map(int,input().split()))
c=sum(c)
if a<c:
  print(-1)
else:
  print(a-c)