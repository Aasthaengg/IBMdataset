n = input()

rcount = 0
m = 0
for i in n:
  if i == "R":
    rcount += 1
  else:
    rcount = 0
  
  if m <= rcount:
    m = rcount
print(m)