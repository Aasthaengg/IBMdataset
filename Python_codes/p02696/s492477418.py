from math import floor
a, b, n = map(int, input().split())
n = min(b-1, n)
ans = floor(a*(n)/b) - a*floor((n)/b)
print(ans)