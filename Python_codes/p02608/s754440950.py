n = int(input())

res = [0] * (n+1)
x = 1
while x*x <= n:
  y = 1
  while y*y <= n:
    z = 1
    while z*z <= n:
      w = x*x+y*y+z*z+x*y+y*z+z*x
      if w <= n:
        res[w] += 1
      z += 1
    y += 1
  x+= 1
  
for i in range(1,n+1):
  print(res[i])