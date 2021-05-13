a=input()
a=int(a)
b=input()
c=""
if a>=len(b):
  print(b)
else:
  for i in range(a):
    c=c+b[i]
  print(c+"...")