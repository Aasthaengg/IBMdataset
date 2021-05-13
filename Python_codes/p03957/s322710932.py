S = input()

a = 0

for i in S:
  if a == 0 and i == "C":
    a += 1
  if a == 1 and i == "F":
    a += 1
    
if a == 2:
  print ("Yes")
else:
  print ("No")