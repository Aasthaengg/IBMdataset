s = input()
ans = 0
p = -1
i = 0
while i-p<len(s):
  if s[i]==s[p]:
    i += 1
    p -= 1
    continue
  elif s[i]=='x':
    i += 1
    ans += 1
  elif s[p]=='x':
    p -= 1
    ans += 1
  else:
    print(-1)
    break
else:
  print(ans)