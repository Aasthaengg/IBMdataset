key = input()

i = 0

if key[i] == key[i+1] or key[i+1] == key[i+2] or key[i+2] == key[i+3]:
  print('Bad')
else :
  print('Good')