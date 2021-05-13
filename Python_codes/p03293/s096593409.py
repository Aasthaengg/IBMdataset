s = input()
t = input()
ans = 'No'
for i in range(len(s)):
  s = s[-1] + s[:-1]
  if s == t:
    ans = 'Yes'
    break
print(ans)