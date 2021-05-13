n = int (input ())
x = 1
for i in range (n):
  x = x*(i+1)
  x = x%(10**9+7)
print (x)