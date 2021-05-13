s = input()
l = 0
r = len(s)-1

flag = True
ans = 0
while l < r:
  if s[l] == s[r]:
    l += 1
    r -= 1
  elif s[l] == "x":
    l += 1
    ans += 1
  elif s[r] == "x":
    r -= 1
    ans += 1
  else:
    flag = False
    break

if flag:
  print(ans)
else:
  print(-1)
