s = list(map(int, input()))
l = [0]*2
l[0] = s[0]*10 + s[1]
l[1] = s[2]*10 + s[3]

F = False
L = False

if 0 < l[0] <= 12:
  F = True
if 0 < l[1] <= 12:
  L = True

if F == True and L == True:
  print('AMBIGUOUS')

elif F == True:
  print('MMYY')

elif L == True:
  print('YYMM')

else:
  print('NA')