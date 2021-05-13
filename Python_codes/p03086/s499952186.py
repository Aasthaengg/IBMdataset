S = input()
T = S.replace('A','1').replace('C','1').replace('G','1').replace('T','1')
a = 0
for s in range(10):
  if '1'*(10-s) in T:
    a=1
    print(10-s)
    break
if a == 0:
  print('0') 