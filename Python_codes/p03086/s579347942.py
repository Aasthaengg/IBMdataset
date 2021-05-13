a=0
b=0
for s in input():
  if s in ['A','C','G','T']:
    b+=1
  else:
    b=0
  a=max(a,b)
print(a)