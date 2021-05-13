s = input()
a = ""
b = ""
ans = 0
for i in range(len(s)):
  b += s[i]
  if a == b:
    continue
  else:
    ans += 1
    a = b
    b = ""
print(ans)