def ABS(a,b):
  c = a - b
  if c < 0:
    c = c * -1
  return c

str = input()
nli = list(map(int,str.split()))

if ABS(nli[0],nli[1]) < ABS(nli[0],nli[2]):
  print("A")
else:
  print("B")