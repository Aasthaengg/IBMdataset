n,m = list(map(int,input().split()))
a = list(map(int,input().split()))

d = 0
for i in range(m):
  d += a[i]
  
ans = n-d
if ans < 0:
  print(-1)
else:
  print(ans)
