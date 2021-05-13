H = int(input())
for i in range(10000):
  if 2**(i-1) <= H < 2**i:
    print(2**i-1)
    break