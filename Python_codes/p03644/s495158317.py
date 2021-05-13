N = int(input())
i = 0
while True:
    if 2**i > N:
        print(2**(i-1))
        exit()
    i += 1