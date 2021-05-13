s = str(input())
L = []
for i in s:
  if i in L:
    print('no')
    exit()
  else:
    L.append(i)
print('yes')