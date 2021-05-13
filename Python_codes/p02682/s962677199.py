a,b,c,k = [int(x) for x in input().split()]
ans = 0
if k <= a:
  ans += k
elif k <= a + b:
  ans += a
else:
  ans += a - (k - a - b)
print(ans)