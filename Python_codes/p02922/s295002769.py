import math
A, B = map(int, input().split())
n = B // A
n2 = math.ceil((B - A * n + (n - 1)) / (A-1))
print(n+n2)