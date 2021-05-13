N=int(input())
for i in range(100):
    t=2**i
    if t>N:
        print(2**(i-1))
        exit()