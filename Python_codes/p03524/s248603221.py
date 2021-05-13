s = input()
a = b = c = 0
for i in range(len(s)):
  if s[i] == 'a':
    a += 1
  elif s[i] == 'b':
    b += 1
  elif s[i] == 'c':
    c += 1
maxv = max(a, max(b, c))
if (maxv-a > 1) or  (maxv-b > 1) or  (maxv-c > 1):
  print("NO")
else:
  print("YES")