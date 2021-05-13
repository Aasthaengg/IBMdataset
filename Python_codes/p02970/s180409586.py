import math
n, k = list(map(int,input().split(' ')))
print(math.ceil(n / ((k * 2) + 1)))
