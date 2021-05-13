import math

n = int(input())
lis = [int(input()) for i in range(n)]

t = lis[0]

for i in range(1, n):
    a = lis[i]
    t = (a*t)//math.gcd(t, lis[i])

print(t)