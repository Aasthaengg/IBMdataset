s, t = [input() for i in range(2)]
ans = 0
for i in range(len(s)):
  if s[i] != t[i]:
    ans += 1
print(ans)