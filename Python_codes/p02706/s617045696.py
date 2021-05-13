m,n,*aa = map(int, open(0).read().split())
ans = m-sum(aa)
if ans<0:
  print(-1)
else:
  print(ans)