import math
N = int(input())
second = math.ceil(N / 1000)
print(second * 1000 - N)