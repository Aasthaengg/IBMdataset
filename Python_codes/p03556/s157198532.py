N=int(input())
for i in reversed(range(1,N+1)):
  if (i**.5).is_integer():
    print(i)
    exit()