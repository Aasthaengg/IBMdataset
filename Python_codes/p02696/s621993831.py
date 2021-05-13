import math

A, B, N = map(int, input().split())
print(math.floor((A * min(B-1, N)) / B) - A * math.floor(min(B-1, N) / B))