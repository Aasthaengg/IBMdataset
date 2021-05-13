l = []
while True:
  s = str(input())
  if s == '-':
    break
  n = int(input())
  for i in range(n):
    t = int(input())
    s = s[t:len(s)] + s[0:t]
  l.append(s)
for a in l:
  print(a)
