N = int(input())

for i in range(100000):
    if 2**i <= N and N<2**(i+1):
        print((2**(i+1))-1)
        break
