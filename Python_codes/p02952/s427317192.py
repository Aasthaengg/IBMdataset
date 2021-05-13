import math
N = int(input())
print(sum([int(math.log10(x)) % 2 == 0 for x in range(1, N + 1)]))