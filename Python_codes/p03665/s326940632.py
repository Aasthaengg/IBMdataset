N, P = map(int, input().split())
A = list(map(int, input().split()))

def nCr(n, r):
    r = min(r, n-r)

    numerator = 1
    for i in range(n, n-r, -1):
        numerator *= i

    denominator = 1
    for i in range(r, 1, -1):
        denominator *= i

    return numerator // denominator

x = sum(A) % 2

o = 0
e = 0

for a in A:
    if a % 2 == 0:
        e += 1
    else:
        o += 1

z = 2**e

y = 1
if P == 0:
    y = 0
if x:
    y ^= 1
res = 0
for i in range(y, o+1, 2):
    res += nCr(o, i)
    
print(res*z)