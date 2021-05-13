n = int(input())
S = [input() for _ in range(n)]
U = []
L = []
for s in S:
  l, r = 0, 0
  for t in s:
    if t == "(":
      r += 1
    else:
      if r > 0:
        r -= 1
      else:
        l += 1
  if l <= r:
    U.append((l, r-l))
  else:
    L.append((r, l-r))
U.sort()
L.sort()
s, t = 0, 0
for a, c in U:
  if s < a:
    print("No")
    exit()
  s += c
for a, c in L:
  if t < a:
    print("No")
    exit()
  t += c
if s != t:
  print("No")
  exit()
print("Yes")