k = 0
for i in input():
  k += i=="S" or -(k>0)
print(k*2)