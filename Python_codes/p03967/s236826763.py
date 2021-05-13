s = input()

d = 0
ans = 0

for m in s:
  if m == "g":
    if d == 0:
      d += 1
    elif d != 0:
      ans += 1
      d -= 1

  elif m == "p":
    if d == 0:
      ans -= 1
      d += 1
    elif d != 0:
      d -= 1

print(ans)