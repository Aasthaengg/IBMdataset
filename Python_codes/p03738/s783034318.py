import sys
a=input().strip()
b=input().strip()

if a==b:
  print("EQUAL")
elif len(a)>len(b):
  print("GREATER")
elif len(b)>len(a):
  print("LESS")
else: #same len
  for i in range(len(a)):
    if int(a[i])>int(b[i]):
      print("GREATER")
      sys.exit()
    elif int(a[i])<int(b[i]):
      print("LESS")
      sys.exit()
