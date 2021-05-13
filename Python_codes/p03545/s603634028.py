x = input()
y = x[0] + 't' + x[1] + 't' + x[2] + 't' + x[3]
for i in range(8):
  for j in range(3):
    if ((i>>j) & 1) == 1:
      z = list(y)
      z[5-2*j] = '+'
      y = ''.join(z)
    else:
      z = list(y)
      z[5-2*j] = '-'
      y = ''.join(z)
      
  if eval(y) == 7:
    print(y+ '=7')
    break