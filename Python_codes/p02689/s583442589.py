n,m=map(int,input().split())
h=list(map(int,input().split()))
flag=[True for _ in range(n)]
for i in range(m):
  a,b=map(int,input().split())
  if h[a-1] >= h[b-1]:
    flag[b-1] = False 
  if h[b-1] >= h[a-1]:
    flag[a-1] = False 
print(flag.count(True))