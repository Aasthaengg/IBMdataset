a, b, c = [int(i) for i in input("").split(" ")]
ispoor = False
if (a == b and b != c):
  ispoor = True
if (b == c and c != a):
  ispoor = True
if (c == a and a != b):
  ispoor = True
if(ispoor):
  print('Yes')
else:
  print('No')