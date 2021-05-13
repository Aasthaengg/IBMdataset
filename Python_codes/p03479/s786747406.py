X, Y = map(int, input().split())

ans = 1
n = 1
a = X
while a <= Y:
  a = X * (2 ** n)
  if a <= Y:
    ans += 1
    n += 1
  else:
    break

print(ans)