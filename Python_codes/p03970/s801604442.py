s = input()
r = "CODEFESTIVAL2016"
ans = 0
for i in range(len(s)):
  if s[i] != r[i]: ans += 1
print(ans)