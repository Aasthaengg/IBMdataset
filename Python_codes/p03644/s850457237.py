n=int(input())
for i in range(1,7):
  if 2**i>n:
    print(2**(i-1))
    break
else:
  print(2**i)