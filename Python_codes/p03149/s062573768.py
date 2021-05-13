N = map(int, input().split())
dic = {1: False, 9: False, 7: False, 4: False}

for n in N:
  dic[n] = True

if all(dic.values()):
  print('YES')
else:
  print('NO')