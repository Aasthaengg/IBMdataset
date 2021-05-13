from math import ceil
n, *cities = [int(input()) for _ in range(6)]

print(ceil(n / min(cities)) + 4)