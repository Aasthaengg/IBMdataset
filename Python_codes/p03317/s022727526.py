from math import ceil

n, k = [int(i) for i in input().split()]
a = [int(i) for i in input().split()]

print(ceil((n-1)/(k-1)))
