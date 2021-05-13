import math
H = int(input())
W = int(input())
N = int(input())
print(min(math.ceil(N / H), math.ceil(N / W)))