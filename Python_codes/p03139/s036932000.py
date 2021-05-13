n,a,b = map(int,input().split())
mx = min(a,b)
if a+b > n:
  mi = a+b -n
else:
  mi = 0
print(mx,mi)