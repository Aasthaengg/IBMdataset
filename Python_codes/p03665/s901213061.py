import math
n,p = map(int,input().split())
ls = list(map(int,input().split()))
lo = []
le = []
def combinations_count(n, r): #組み合わせ(nCr)
    return math.factorial(n) // (math.factorial(n - r) * math.factorial(r))
for i in ls:
    if i % 2 == 0:
        le.append(i)
    else:
        lo.append(i)
x = len(lo)
y = len(le)
if p == 0:
    a = 1
    if x != 0:
        if x % 2 == 0:
            r = x
        else:
            r = x - 1
        a = 0
        for j in range(0,r+1,2):
            a += combinations_count(x, j)
    b = 1
    if y != 0:
        b = 0
        for k in range(y+1):
            b += combinations_count(y, k)
    print(a*b)
else:
    if x != 0:
        if x % 2 == 0:
            r = x - 1
        else:
            r = x
        a = 0
        for j in range(1,r+1,2):
            a += combinations_count(x, j)
    else:
        a = 0
    b = 1
    if y != 0:
        b = 0
        for k in range(y+1):
            b += combinations_count(y, k)
    print(a*b)
