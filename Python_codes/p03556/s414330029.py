n= int(input())

for i in range(n,-1,-1):
  if (i**0.5).is_integer():
    print(i)
    break