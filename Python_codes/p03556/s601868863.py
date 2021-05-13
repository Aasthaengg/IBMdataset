n=int(input())
for i in range(1,40000):
  if i**2>n:
    print((i-1)**2)
    break