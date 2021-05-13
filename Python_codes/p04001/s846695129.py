x = input()
l = len(x)
y_original = x[0]
s = 0

for i in range(1,l):
  y_original += 't'+x[i]
  
for i in range(2**(l-1)):
  y = y_original
  for j in range(l-1):  
    if ((i>>j) & 1) == 1:
      z = list(y)
      z[(2*l-3)-2*j] = '+'
      y = ''.join(z)
  y2 = y.replace('t','')
  s += eval(y2)
print(s)