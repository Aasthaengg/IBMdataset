a = int(input())
b = int(input())
h = int(input())

if a>b:
  print(int((((a-b)*h)/2)+(b*h)))
elif b>a:
  print(int((((b-a)*h)/2)+(a*h)))
else:
  print(int(a*h))