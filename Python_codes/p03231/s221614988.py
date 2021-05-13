#import sys
n, m = map(int, input().split())
s = input()
t = input()

if s[0] != t[0]:
    print(-1)
    exit()
    #sys.exit(0)

#a,bの最大公約数
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

#a,bの最小公倍数
def lcm(a, b):
    return a * b // gcd (a, b)

l = lcm(n, m)
step = min(l//n, l//m)

for i in range(0, l, step):
    if i % (l//n) == 0 and i % (l//m) == 0:
        if s[i * n // l] != t[i * m // l]:
            print(-1)
            exit()
            # sys.exit(0)

print(l)
