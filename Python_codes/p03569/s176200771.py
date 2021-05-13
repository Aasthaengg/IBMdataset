import re
s = input()
t = s.replace("x", "")
if t != t[::-1]:
  print(-1)
else:
  k = re.split('[abcdefghijklmnopqrstuvwyz]', s)
  l = len(k)
  ans = 0
  for i in range(l//2):
    ans += abs(len(k[i]) - len(k[l-1-i]))
  print(ans)