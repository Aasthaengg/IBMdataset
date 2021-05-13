s = input()
ans = 0
for i in range(len(s)):
  if s.count(s[i]) == 2:
    ans += 1
    
if ans == 4:
  print('Yes')
else:
  print('No')