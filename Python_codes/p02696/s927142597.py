import math

a, b, n = map(int, input().split())

M = 0
t = min(b-1, n)
M = math.floor(a*t/b) - a*math.floor(t/b)

print(M)