n=int(input())
for i in range(7):
  if 2**(i+1) > n:
    print(2**i)
    break