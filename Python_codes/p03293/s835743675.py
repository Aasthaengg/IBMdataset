s = input()
t = input()
ans = "No"
for i in range(len(s)):
  if s[i:] + s[0:i] == t:
    ans = "Yes"
print(ans)