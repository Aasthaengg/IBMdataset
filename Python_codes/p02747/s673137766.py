S = input()

HI ='hi'

flag = False

for i in range(5):
  if S == HI * (i +1):
    flag = True
    break

if flag == True:
  print('Yes')
else:
  print('No')