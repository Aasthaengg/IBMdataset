import math

n, k = map(int, input().split())
a = map(int, input().split())

print(math.ceil((n-1)/(k-1)))