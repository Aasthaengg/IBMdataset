a = input()
s = a.find(' ')
a+= "."
b = a[s+1:-1]
a= a[0:s]
a=int(a)
b=int(b)
c= int(b/2)
if a>12:
  print(b)
elif a<=12 and a>=6:
  print(c)
else:
  print(0)