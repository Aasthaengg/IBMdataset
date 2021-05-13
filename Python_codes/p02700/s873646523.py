a, b, c, d = map(int, input().split())
e = a // d 
f = c // b
if(a % d):
  e += 1
if(c % b):
  f += 1

if(e >= f):
  print("Yes")
else:
  print("No")