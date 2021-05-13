n,m=map(int,input().split())
h=list(map(int,input().split()))
e=[1]*n
for _ in range(m):
  a,b=map(int,input().split())
  if h[a-1]>h[b-1]:e[b-1]=0
  elif h[a-1]<h[b-1]:e[a-1]=0
  else:
    e[a-1]=0
    e[b-1]=0
print(sum(e))