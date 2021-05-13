Sa=list(str(input()))
Sb=list(str(input()))
Sc=list(str(input()))
card=Sa.pop(0)
while 1:
  if card=='a':
    if len(Sa)==0:
      print('A')
      break
    card=Sa.pop(0)
  elif card=='b':
    if len(Sb)==0:
      print('B')
      break
    card=Sb.pop(0)
  elif card=='c':
    if len(Sc)==0:
      print('C')
      break
    card=Sc.pop(0)
