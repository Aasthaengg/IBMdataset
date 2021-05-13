x = int(input())
aa, bb = 0, 0
for i in range(-200, 200):
  for j in range(-200, 200):
    if(i**5 - j**5 == x):
      aa, bb = i, j
    if(aa != 0 or bb != 0):
      break
  if(aa != 0 or bb != 0):
    break
print(str(aa) + " " + str(bb))