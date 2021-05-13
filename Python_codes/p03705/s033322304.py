n,a,b = map(int,input().split())
mx = a + (n-1)*b
mi = (n-1)*a + b
ans = mx - mi + 1
if n == 1 and a != b or a > b:
  print(0)
else:
  print(ans)