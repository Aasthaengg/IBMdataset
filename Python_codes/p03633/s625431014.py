import math
N = int(input())

t1 = 1
for i in range(N):
    t2 = int(input())
    t1 = (t1 * t2) // math.gcd(t1, t2)

print(t1)