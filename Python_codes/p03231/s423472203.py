from math import gcd
from sys import exit
n, m = map(int, input().split())
s = input()
t = input()
x = gcd(n, m)
y = n * m // x
a = n // x
b = m // x
for i in range(x):
    if s[i * a] != t[i * b]:
        print(-1)
        exit()
print(y)