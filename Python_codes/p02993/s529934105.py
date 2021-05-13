S = input()
flag = False
tmp = ''
for s in S:
  if tmp == s:
    flag = True
  tmp = s
if flag == True:
  print('Bad')
else:
  print('Good')