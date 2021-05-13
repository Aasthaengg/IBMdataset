s=input()
ct=0
for i in s:
  if i=='o':
    ct+=1
if 15-len(s)+ct>=8:
  print('YES')
else:
  print('NO')
