S = input()
Sl = list(S)

if Sl[0] == Sl[1]:
  print('Bad')
elif Sl[1] == Sl[2]:
  print('Bad')
elif Sl[2] == Sl[3]:
  print('Bad')
else:
  print('Good')