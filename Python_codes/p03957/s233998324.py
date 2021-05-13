s = input()
ans = []

for i in range(len(s)):
  if len(ans) == 0 and s[i] == 'C':
    ans.append(s[i])
  elif len(ans) == 1 and s[i] == 'F':
    ans.append(s[i])

if len(ans) == 2 and ans[0] == 'C' and ans[1] == 'F':
  print('Yes')
else:
  print('No')