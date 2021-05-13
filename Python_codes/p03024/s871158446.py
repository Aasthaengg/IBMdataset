s = input()
cnt = 0
for _s in s:
  if _s == "o":
    cnt += 1
if cnt + 15 - len(s) >= 8:
  print("YES")
else:
  print("NO")