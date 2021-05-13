x=int(input())

for a in range(-140,140):
  for b in range(-140,140):
    if (a**5-b**5)==x:
      c=a
      d=b
      break
      
print(str(c)+' '+str(d))