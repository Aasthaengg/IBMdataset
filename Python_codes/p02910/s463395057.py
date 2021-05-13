S=input()
L={'U','D','L'}
R={'U','D','R'}
for i in range(len(S)):
  if i%2==0:
    if not S[i] in R:
      print('No')
      exit()
  else:
    if not S[i] in L:
      print('No')
      exit()
else:
  print('Yes')