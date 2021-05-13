from fractions import gcd
n = int(input())
a = [int(i) for i in input().split()]
g = a[0]
for i in a[1:]:
    g = gcd(g, i)
    if g == 1:
        break
print(g)