n, m = map(int, input().split())
x = [list(map(int, input().split())) for _ in range(n)]
x.sort()

s = 0
for a, b in x:
  if m > b:
    s += a * b
    m += -b
  else:
    s += a * m
    break

print(s)