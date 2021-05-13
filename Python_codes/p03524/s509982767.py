s = input()

na = nb = nc = 0
for c in s:
  if c == 'a':
    na += 1
  if c == 'b':
    nb += 1
  if c == 'c':
    nc += 1

if abs(na - nb) < 2 and abs(na - nc) < 2 and abs(nb - nc) < 2:
  print("YES")
else:
  print("NO")
