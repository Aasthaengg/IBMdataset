S = input()

if len(S) == 2:
  print(S)
else:
  result = []
  listS = list(S)
  for i in range(3):
    result.append(listS[2 - i])
  print(''.join(result))