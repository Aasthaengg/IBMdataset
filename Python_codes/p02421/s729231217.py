t = 0; h = 0
for _ in range(int(input())):
  a, b = map(str, input().split())
  if a == b:
    t += 1
    h += 1
    continue
  l = sorted([a, b])
  if [a, b] == l:
    h += 3
  else:
    t += 3
print("{0} {1}".format(t, h))
