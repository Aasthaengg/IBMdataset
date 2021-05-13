n, k = map(int, input().split())
a = list(map(int , input().split()))

if n == k:
    print(1)
    exit()
import math
print(1 + math.ceil(((n - k) / (k-1))))