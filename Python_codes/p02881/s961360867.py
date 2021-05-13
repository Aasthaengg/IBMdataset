import math
N = int(input())
for i in reversed(range(1, int(math.sqrt(N)) + 1)):
    if N % i == 0:
        print(i + (N // i) - 2)
        quit()