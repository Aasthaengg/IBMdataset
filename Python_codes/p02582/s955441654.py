S = input()
 
a = (S[0] == 'R')
b = (S[1] == 'R')
c = (S[2] == 'R')
 
if a and b and c:
  print(3)
elif (a and b and (c == False)) or ((a == False) and b and c):
  print(2)
elif (a == False) and (b == False) and (c == False):
  print(0)
else:
  print(1)