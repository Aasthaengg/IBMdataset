S = input()
C = []
for i in range(len(S)):
  if S[i] in C:
    print('no')
    break
  C.append(S[i])
else:
  print('yes')