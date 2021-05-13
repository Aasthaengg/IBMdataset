a, b, c, d = map(int, input().split())
if a*b>c*d:
  ans = a*b
else:
  ans = c*d
print(ans)