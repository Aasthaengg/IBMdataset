S = input()
temp = S[0]
temp1 = '0'
a = 1
b = 0
c = 0
for i in range(1,4):
  if temp == S[i]:
    a = a+1
  elif temp1 == S[i]:
    c = c+1
  else:
    temp1 = S[i]
    b = b+1
if b == 1 and a == 2 and c == 1:
  print('Yes')
else:
  print('No')