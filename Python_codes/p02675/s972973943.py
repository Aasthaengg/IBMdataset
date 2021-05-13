n=input()
a=['2','4','5','7','9']
b=['0','1','6','8']
h=n[-1] in a
p=n[-1] in b
if h==1:
  print('hon')
elif p==1:
  print('pon')
else:
  print('bon')