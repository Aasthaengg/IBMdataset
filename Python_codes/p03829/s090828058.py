n, a, b = map(int, input().split())
x = list(map(int, input().split()))

hp = 0
good = min(a, b)
bad = max(a, b)

if good == a:
  for i in range(n):
    if i+1 == n:
      break
    if bad >= abs(x[i+1] - x[i])*good:
      hp += abs(x[i+1] - x[i]) * good
    else:
      hp += bad

else:
  for i in range(n):
    if i+1 == n:
      break
    if good >= abs(x[i+1] - x[i])*bad:
      hp += abs(x[i+1] - x[i]) * bad
    else:
      hp += good
print(hp)