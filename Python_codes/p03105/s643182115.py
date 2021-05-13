a, b, c = map(int, input().split())

if a * c <= b:
  ans = c
else:
  ans = b // a

print(ans)
