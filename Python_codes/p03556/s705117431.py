N = int(input())
a = int((N+1)**0.5)
if a**2>N:
  ans = (a-1)**2
else:
  ans = a**2
print(ans)
