s = input()

v = 'abcdefghijklmnopqrstuvwxyz'
ans = 1000
for i in range(26):
  t = s
  a = t.split(v[i])
  if len(a) == 1:
    continue
  b = 0
  for j in a:
    b = max(len(j),b)
  ans = min(b,ans)
print (ans)
