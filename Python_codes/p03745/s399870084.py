p = -1
xp = -1
ans = 1
input()
for i in input().split(" "):
  i = int(i)
  if i == p: continue
  if p != -1:
    x = p < i
    if xp != -1:
      ans += x != xp
    if xp != -1 and x != xp:
      xp = -1
    else:
      xp = x
  p = i
print(ans)
