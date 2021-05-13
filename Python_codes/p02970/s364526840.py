from math import ceil
n,d = [int(z) for z in input().split()]

n = n/(2*d+1)
print(ceil(n))
