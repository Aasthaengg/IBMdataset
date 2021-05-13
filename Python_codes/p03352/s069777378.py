x = int(input())
c = []

for b in range(1,x+1):
  for q in range(2,x+2):
    a = b**q
    if a <=x:
      c.append(a)
    else:
      break

C = set(c)
print(max(C))
