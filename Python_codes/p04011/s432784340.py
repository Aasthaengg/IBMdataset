n = input()
k = input()
x = input()
y = input()

n = int(n)
k = int(k)
x = int(x)
y = int(y)

if(n<k):
  print(n*x)
else:
  print((k)*x + y*(n-k))
