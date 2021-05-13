S = input()
O = ['R','U','D']
E = ['L','U','D']
ng = False
for i in range(len(S)):
  if i % 2 == 0:
    if S[i] not in O:
      ng = True
      break
  else:
    if S[i] not in E:
      ng = True
      break
print('No') if ng else print('Yes')
