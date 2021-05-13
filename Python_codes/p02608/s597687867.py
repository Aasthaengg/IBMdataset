n = int(input())

a = [0]*10001

for x in range(1, 101):
  for y in range(1, 101):
    for z in range(1,101):
        v = x*x+y*y+z*z+x*y+y*z+x*z
        if  v < 10001:
        	a[v] += 1
for i in range(n):
  print(a[i+1])