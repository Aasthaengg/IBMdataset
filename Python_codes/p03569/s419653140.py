s = input()
if len(s) == 1:
  print(0)
  exit()
l = 0
r = len(s) - 1
cnt = 0
while l < r:
  if s[l] == s[r]:
    l += 1
    r -= 1
  else:
    if s[l] == "x":
      l += 1
      cnt += 1
    elif s[r] == "x":
      r -= 1
      cnt += 1
    else:
      print(-1)
      exit()
print(cnt)