intx = input().split()
product = (int(intx[0]) * int(intx[1]))
remainder = product % 2

if remainder == 1:
  print("Odd")
else:
  print("Even")