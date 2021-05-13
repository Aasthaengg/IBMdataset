a, b = map(int, input().split())

def f(x):
  if x == 1:
    return 300000
  if x == 2:
    return 200000
  if x == 3:
    return 100000
  return 0

ans = f(a) + f(b)
if a == 1 and b == 1:
  ans += 400000
print(ans)