n, a, b = map(int, input().split())

x = list(map(int, input().split()))
xp = x[0]
ans = 0

for xi in x[1:]:
  ans += min((xi-xp)*a, b)
  xp = xi
  
print(ans)