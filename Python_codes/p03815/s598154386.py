x = int(input())
 
s = x//11
 
if 11*s == x:
  print(s*2)
elif x <= 11*s + 6:
  print(s*2+1)
else:
  print(s*2+2)
