n = int(input())
a = list(map(int, input().split()))

a.sort()

posi = [a[-1]]
nega = [a[0]]

for n in a[1:-1]:
  if n < 0:
    nega.append(n)
  else:
    posi.append(n)

selected = []
ans = nega[0]

for n in posi[1:]:
  (x, y) = ans, n
  ans = x - y
  selected.append((x, y))

nega.append(ans)

ans = posi[0]
for n in nega[1:]:
  (x, y) = ans, n
  ans = x - y
  selected.append((x, y))

print(ans)

for (x, y) in selected:
  print(str(x) + ' ' + str(y))


