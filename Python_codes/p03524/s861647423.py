s = input()

na = nb = nc = 0
for c in s:
  if c == 'a':
    na += 1
  if c == 'b':
    nb += 1
  if c == 'c':
    nc += 1

if max(abs(na-nb), max( abs(na - nc), abs(nb - nc))) > 1:
  print("NO")
else:
  print("YES")
