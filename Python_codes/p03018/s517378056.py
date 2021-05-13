s = input()
if 'BC' not in s:
  print(0)
  import sys
  sys.exit()
t = s.split('BC')
m = 0
ans = 0
for l in t[:-1]:
  cnt = 0
  for i in range(len(l)-1,-1,-1):
    if l[i]!='A':
      ans += cnt
      m = cnt
      break
    cnt += 1
  else:
    m += cnt
    ans += m
print(ans)
