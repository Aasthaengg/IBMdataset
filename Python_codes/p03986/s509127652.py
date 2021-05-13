s = input()
 
l = 0
r = 0
for si in s:
  if si == "S":
    r += 1
  else:
    if r == 0:
      l += 1
    else:
      r -= 1
ans = l + r
print(ans)