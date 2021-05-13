#14:43(2)
n,k = map(int,input().split())
if k % 2 == 1:
  r = n//k
  s = 0
else:
  r = n//k
  s = n//(k//2) - r
print(r**3+s**3)