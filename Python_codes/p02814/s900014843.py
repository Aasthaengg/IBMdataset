from math import gcd, ceil
n, m = map(int, input().split())
a = list(map(int, input().split()))
a = [i // 2 for i in a]
l = 1
for i in a:
    l *= i // gcd(l, i)
for i in a:
    if l // i % 2 == 0:
        print(0)
        exit()
print(ceil((m // l) / 2))