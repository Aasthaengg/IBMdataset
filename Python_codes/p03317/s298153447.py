from math import ceil
n,k = map(int, input().split())
a = list(map(int, input().split()))

m = a.index(1)
print(ceil((n-1)/(k-1)))