O=[x for x in input()]
E=[y for y in input()]

for i in range(max(len(O),len(E))):
  try:
    print(O[i],end='')
  except:
    pass
  try:
    print(E[i],end='')
  except:
    pass