x = int(input())
c = 1

for b in range(1,x):
  for q in range(2,x):
    if b**q <=x:
      c = max(c,b**q)
    else:
      break
print(c)