n,m=map(int,input().split())
d=[0 for i in range(n)]
for i in range(m):
  a,b=map(lambda x:int(x)-1,input().split())
  d[a]^=1
  d[b]^=1

print("NO" if sum(d) else "YES")