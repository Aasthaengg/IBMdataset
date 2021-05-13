A,B = map(int, input().split())

ans = None

if A+B > 23:
  ans = A+B-24
else:
  ans = A+B
print(ans)
