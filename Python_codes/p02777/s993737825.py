x = input().split()

s = x[0]
t = x[1]

y = input().split()

a = int(y[0])
b = int(y[1])

u = input()

if(u == s):
  print(a-1,b)
else:
  print(a,b-1)