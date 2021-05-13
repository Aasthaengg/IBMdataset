a = int(input())

for i in range(1, int(a ** .5)+2):
  if i ** 2 > a:
    print((i-1)**2)