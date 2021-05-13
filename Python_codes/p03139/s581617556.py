n,a,b = map(int, input().split())
ma = min(a,b)
if a+b <=n:
  mi = 0
elif a+b >n:
  mi = abs(n-(a+b))
print(ma,mi)