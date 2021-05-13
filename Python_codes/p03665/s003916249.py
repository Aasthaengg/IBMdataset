import math

def comb(n, r):
    return math.factorial(n) // (math.factorial(n - r) * math.factorial(r))

n, p = map(int, input().split())
l = list(map(int, input().split()))

o = 0
e = 0
for i in range(n):
    if l[i] % 2 == 0:
        e += 1
    else:
        o += 1

if p == 0:
    a = 0
    for i in range(e+1):
        a += comb(e, i)
    b = 0
    for i in range(0, o+1, 2):
        b += comb(o, i)
    print(a*b)

else:
    a = 0
    for i in range(e+1):
        a += comb(e, i)
    b = 0
    for i in range(1, o+1, 2):
        b += comb(o, i)
    print(a*b)
   