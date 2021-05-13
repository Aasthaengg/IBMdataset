n, a, b = map(int, input().split())
H = [int(input()) for _ in range(n)]
c = a - b
def is_can(x):
  s = 0
  d = b*x
  for h in H:
    s += max(0, -(-(h-d) // c))
  if s <= x:
    return True
  return False

ng = 0
ok = -(-max(H)//b)
while ok - ng > 1:
  m = (ok+ng)//2
  if is_can(m):
    ok = m
  else:
    ng = m
print(ok)