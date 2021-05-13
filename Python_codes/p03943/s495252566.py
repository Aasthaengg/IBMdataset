x = list(map(int,input().split()))
a = x[0]
b = x[1]
c = x[2]

if a == b+c or b == a+c or c == a+b:
  print("Yes")
else: 
  print("No")