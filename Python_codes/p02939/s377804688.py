S = input()
now = ""
ans = 0
flag = 0
for s in S:
  if flag == 1:
    now = ""
    ans += 1
    flag = 0
  else:
    if now == s:
      flag = 1
    else:
      now = s
      ans += 1
print(ans)