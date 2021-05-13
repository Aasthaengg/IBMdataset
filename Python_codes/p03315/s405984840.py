s = list(input())
for i in range(len(s)):
  if s[i] == "+":
    s[i] = 1
  else:
    s[i] = -1

print(sum(s))
