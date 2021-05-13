abl = [map(int,input().split()) for nesya in range(3)]
s = [1,1,2,2,3,3,4,4]
c = 0
for ab in abl:
  for n in ab:
    if n in s:
      s.remove(n)
    else:
      c += 1
if c == 0:
  print('YES')
else:
  print('NO')
