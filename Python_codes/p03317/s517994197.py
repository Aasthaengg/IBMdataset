from math import ceil
n, k = [int(x) for x in input().split()]
a_list = [int(x) for x in input().split()]
print(ceil((n - 1) / (k - 1)))