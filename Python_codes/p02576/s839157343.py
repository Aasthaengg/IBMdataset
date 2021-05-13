import math

N,X,T = [int(i) for i in input().split()]
print(math.ceil(N / X) * T)