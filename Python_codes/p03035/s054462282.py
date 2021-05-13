tmp = input().split(" ")
age = int(tmp[0])
fee = int(tmp[1])

if age >= 13:
  print(fee)
elif age >= 6:
  print(int(fee/2))
else:
  print(0)