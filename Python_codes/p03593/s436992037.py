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
mod1 = 1 if oe == 2 else 0
mod2 = (H//2)*(W%2)+(W//2)*(H%2)
mod4 = (H//2)*(W//2)
for _ in range(mod1):
  for c in counts.keys():
    if counts[c] % 4 == 1:
      counts[c] -= 1
      break
for _ in range(mod2):
  for c in counts.keys():
    if counts[c] % 4 == 2:
      counts[c] -= 2
      mod2 -= 1
      break
if mod2 % 2 == 0:
  mod4 += mod2//2
  for _ in range(mod4):
    for c in counts.keys():
      if counts[c] % 4 == 0 and counts[c] > 0:
      	counts[c] -= 4
      	break
  for n in counts.values():
    if n > 0:
      ans = "No"
      break
else:
  ans = "No"
print(ans)
