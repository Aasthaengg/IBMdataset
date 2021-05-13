X = input()

ans = 0
t = 0
for x in X:
  if x == "S":
    t -= 1
  else:
    t += 1
  ans = max(ans, t)

print(ans * 2)