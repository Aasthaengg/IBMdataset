s=input()
t=input()
ans=""
for i in range(max(len(s),len(t))):
  if i < len(s):
    ans += s[i]
  if i < len(t):
    ans += t[i]
print(ans)