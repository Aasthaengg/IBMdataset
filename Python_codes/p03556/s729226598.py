N = int(input())
x = 1
while True:
  if x**2 > N:
    break
  else:
    x +=1
print((x-1)**2)