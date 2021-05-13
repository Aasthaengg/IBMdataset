S=input()
x=['R','U','D']
y=['L','U','D']
l=len(S)
for i in range(l):
  if (i+1)%2!=0:
    if S[i]not in x:
      print('No')
      exit()
  else:
    if S[i] not in y:
      print('No')
      exit()

print("Yes")