H, W = map(int, input().split())
A = [list(input()) for _ in range(H)]
counts = {}
for a_ in A:
  for a in a_:
    if not a in counts:
      counts[a] = 1
    else:
      counts[a] += 1
ans = "Yes"
oe = H%2+W%2
if oe == 0:
  for n in counts.values():
    if n % 4 != 0:
      ans = "No"
      break
elif oe == 1:
  even = H if H % 2 == 0 else W
  modis2 = 0
  for n in counts.values():
    if n % 4 == 2:
      modis2 += 1
      if modis2 > even / 2:
        ans = "No"
        break
    elif n % 4 != 0:
      ans = "No"
      break
else:
  if H == 1 or W == 1:
    oddcount = 0
    for n in counts.values():
      if n % 2 == 1:
        oddcount += 1
        if oddcount > 2:
          ans = "No"
          break
  else:
    modcount = [0] * 4
    for n in counts.values():
      modcount[n%4] += 1
    if modcount[1]+modcount[3] == 1 and modcount[2] + modcount[3] == (H//2)+(W//2):
      ans = "Yes"
    else:
      ans = "No"
print(ans)
