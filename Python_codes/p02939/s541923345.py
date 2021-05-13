s = input()

ans = 0
before = ""
tmp = ""
for i in range(len(s)):
  tmp += s[i]
  if tmp != before:
    ans += 1
    before = tmp
    tmp = ""
  else:
    before = tmp

print(ans)