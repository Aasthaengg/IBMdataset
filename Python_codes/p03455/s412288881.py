a, b = map(int, input().split())
mul = a * b
joyo = mul % 2
if(joyo == 1):
  print("Odd")
else:
  print("Even")