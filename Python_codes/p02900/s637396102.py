a, b = map(int, input().split())
while a > 0:
    a, b = b % a, a
ret = 1
d = 2
while b >= d * d:
    if b % d == 0:
        ret += 1
        while b % d == 0:
            b //= d
    d += 1
if b > 1:
    ret += 1
print(ret)

