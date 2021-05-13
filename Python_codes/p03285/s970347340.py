N= int(input())
a = N//4 + 1
b= N//7+1
f = False
for i in range(0,a+1):
  if f:
    break
  for j in range(0,b+1):
    if N == 4*i+7*j:
      print('Yes')
      f = True
      break

if not f:
  print('No')
    
