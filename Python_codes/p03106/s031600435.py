import math

a, b, k = list(map(int, input().split()))

d = math.gcd(a, b)

e = d + 1
l = 0
while True:
    e -= 1
    if d % e == 0:
        l += 1
        if l == k:
            break


print(e)