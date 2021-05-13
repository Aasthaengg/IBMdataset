from math import gcd
n = int(input())
a = list(map(int,input().split()))
c = gcd(a[0], a[1])
for i in range(2, len(a) - 1):
    c = gcd(c, a[i])
print(c)