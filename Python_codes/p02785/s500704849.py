n,k=map(int,input().split())
h=sorted(list(map(int,input().split())))
ans = 0
if k >= n:
  print(0)
else:
  for i in range(n-k):
    ans += h[i]
  print(ans)