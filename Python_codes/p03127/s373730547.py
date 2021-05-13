from fractions import gcd

n = int(input())
a = list(map(int, input().split()))

g=a[0]
for i in a[1:]:
    g = gcd(g,i)

print(g)