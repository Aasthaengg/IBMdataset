X = input()
p = X[0]
ls = []
cnt = 1
for c in X[1:]:
  if p!=c:
    ls.append(cnt)
    cnt = 1
    p = c
  else:
    cnt += 1
ls.append(cnt)
s = 0
t = 0
m = 0
if X[0]=='S':
  for i in range(len(ls)):
    if i%2==0:
      s += ls[i]
    else:
      t += ls[i]
    if s<t:
      m += t-s
      t = 0
      s = 0
  print(2*m)
else:
  for i in range(len(ls)):
    if i%2==0:
      t += ls[i]
    else:
      s += ls[i]
    if s<t:
      m += t-s
      t = 0
      s = 0
  print(2*m)