s = input()
cnt = 1
maxcnt=1
for i in range(1,4):
  if s[i]==s[i-1]:
    cnt += 1
  else:
    maxcnt = max(cnt,maxcnt)
    cnt=1
maxcnt = max(cnt,maxcnt)
if maxcnt>=2:
  print("Bad")
else:
  print("Good")