n, *a = map(int, open(0))
if a[0] or any(c - b > 1 for b, c in zip(a, a[1:])):exit(print(-1))
b = ans = 0
for c in a[1:]:
  ans += b * (c - b != 1)
  b = c
print(ans + b)