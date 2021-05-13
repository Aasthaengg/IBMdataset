import math

a, b, k = map(int, input().split())
gcd = math.gcd(a, b)
count = 0
for i in range(gcd, 0, -1):
    if gcd % i == 0:
        count += 1
        if count == k:
            print(i)