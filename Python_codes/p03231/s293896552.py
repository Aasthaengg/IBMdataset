import sys
import math


inint = lambda: int(sys.stdin.readline())
inintm = lambda: map(int, sys.stdin.readline().split())
inintl = lambda: list(inintm())
instrm = lambda: map(str, sys.stdin.readline().split())
instrl = lambda: list(instrm())

n, m = inintm()
s = input()
t = input()

c = {}

def lcm(x, y):
    return (x * y) // math.gcd(x, y)

lcm_num = lcm(n,m)

for i in range(n):
    c[i*m + 1] = s[i]

for i in range(m):
    if i*n + 1 in c:
        if c[i*n + 1] != t[i]:
            print(-1)
            exit()

print(lcm_num)