import math

N = int(input())
trans = [int(input()) for i in range(5)]
print(math.ceil(N / min(trans)) - 1 + 5)
