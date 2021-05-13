s = input()
n = len(s)
ans,cnt = 0,0
for i in s[::-1]:
  if i == "W":
    cnt += 1
  else:
    ans += cnt
print(ans)