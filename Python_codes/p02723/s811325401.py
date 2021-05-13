s = input()
ans = []

for p in range(len(s)):
  ans.append(s[p])
if ans[2] == ans[3] and ans[4] == ans[5]:
  print('Yes')
else:
  print('No')