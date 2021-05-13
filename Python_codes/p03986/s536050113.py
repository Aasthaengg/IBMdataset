x = input()
ans = len(x)
cs = 0
T = False

for i in x:
  if i == 'S':
    if T:
      T = False
    cs += 1
  else:
    if not T:
      T = True
    if cs > 0:
      cs -= 1
      ans -= 2
print(ans)