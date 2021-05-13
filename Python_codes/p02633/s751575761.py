X = int(input())
i = 0
Y = X
while Y % 360 != 0:
  Y += X
  i += 1

i += 1  
print(i)