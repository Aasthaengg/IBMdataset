input()
a, b = map(int, input().split())
s = t = u = 0
for p in map(int, input().split()):
  if p <= a:
    s += 1
  elif p <= b:
    t += 1
  else:
    u += 1
print(min(s, t, u))