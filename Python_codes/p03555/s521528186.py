c1 = list(map(str, input()))
c2 = list(map(str, input()))
if c1[2]==c2[0] and c1[1]==c2[1] and c1[0]==c2[2]:
  print('YES')
else:
  print('NO')