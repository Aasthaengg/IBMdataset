n,a,b,c,d,e = map(int,open(0).read().split())
m = min(a,b,c,d,e)
ans = n//m+4
if n%m == 0:
  print(ans)
else:
  print(ans+1)