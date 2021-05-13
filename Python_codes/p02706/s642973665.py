n, m = map(int, input().split())
l=list(map(int, input().split()))
ans= n-sum(l)
if ans>=0:
  print(ans)
else:
  print(-1)