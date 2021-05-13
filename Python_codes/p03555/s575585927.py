for x,y in zip(input(),reversed(input())):
  if x!=y:
    print('NO')
    break
else:
  print('YES')
