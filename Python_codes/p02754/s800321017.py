n, a, b = map(int,input().split())
ans = 0
x = n//(a + b)
ans = ans + x*a
y = n%(a + b)
if (y >= a):
  ans = ans + a
else:
  ans = ans + y
print(ans)