s = list(input())
c = 0
for i in range(len(s)):
  if s[i] != s[::-1][i]:
    s[i] = s[::-1][i]
    c += 1
print(c)