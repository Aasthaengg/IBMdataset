from collections import Counter as C
 
S = input()
 
c = C(S)
if len(c.keys())==2:
  if list(c.values())[0]==2:
    print("Yes")
  else:
    print("No")
else:
  print("No")