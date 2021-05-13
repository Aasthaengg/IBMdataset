S = input()
akb = 'AKIHABAR'
if len(S) <= len(akb)+1:
  i = 0
  for a in akb:
    if i >= len(S):
      print('NO')
      exit()
    if S[i] == a: i+=1
    elif S[i] != a and a == 'A': continue
    else:
      print('NO')
      exit()
  print('YES')
else:
  print('NO')

