import math
N = int(input())
Cap = [int(input()) for X in range(0,5)]
print(int(math.ceil(N/min(Cap))+4))