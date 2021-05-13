import sys
N = int(input())

for h in range(1, 3500):
    for n in range(1, 3500):
        bumbo = 4*h*n - N*n - N*h
        if bumbo > 0:
            if (N*h*n) % bumbo == 0:
                w = (N*h*n) // bumbo
                print(h, n, w)
                sys.exit()