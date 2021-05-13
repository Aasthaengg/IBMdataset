N = int (input ())
p = 0
for i in range (N+1):
  x = 0
  for j in range (i+1):
    if i%(j+1) == 0 and i%2 == 1:
      x += 1
  if x == 8:
    p += 1
print (p)