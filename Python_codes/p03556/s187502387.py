import math
N = int(input())

while True:
    if math.sqrt(N) % 1 == 0:
        print(N)
        exit()
    N -= 1