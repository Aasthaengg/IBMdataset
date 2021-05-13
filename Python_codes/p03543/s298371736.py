s = input()
cnt = 1
maxcnt=1
for i in range(1,4):
  if s[i] == s[i-1]:
    cnt += 1
  else:
    maxcnt = max(maxcnt,cnt)
    cnt = 1
maxcnt = max(maxcnt,cnt)
if maxcnt>=3:
  print("Yes")
else:
  print("No")