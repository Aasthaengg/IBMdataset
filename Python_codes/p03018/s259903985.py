s = input()
cnt = 0
flg = 0
ans = 0
for i in range(len(s)-1):
  if s[i] == "A":
    if flg == 0:
      cnt += 1
    else:
      cnt = 1
  elif s[i:i+2] == "BC":
    ans += cnt
    flg = 1
  elif flg == 1:
    flg = 0
    continue
  else:
    cnt = 0
print(ans)