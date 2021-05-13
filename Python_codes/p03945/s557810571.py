s = input()

cnt = 0
back = s[0]
for i in range(1, len(s)):
  if back != s[i]:
    cnt += 1
  back = s[i]
print(cnt)