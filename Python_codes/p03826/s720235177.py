lengthArray = list(map(int,input().split()))

a = lengthArray[0]*lengthArray[1]
b = lengthArray[2]*lengthArray[3]

if a<b:
  print(b)
else:
  print(a)
