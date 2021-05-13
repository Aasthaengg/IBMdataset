import math

N = int(input())
A = sorted(list(map(int,input().split())))
d = [0]*(10**6+2)
d[1] = 1
def make_divisors(n):
    lower_divisors , upper_divisors = [], []
    i = 1
    while i*i <= n:
        if n % i == 0:
            lower_divisors.append(i)
            if i != n // i:
                upper_divisors.append(n//i)
        i += 1
    return lower_divisors + upper_divisors[::-1]

f = 1
for e in A:
    for y in make_divisors(e):
        if y == 1:
            continue
        if d[y] != 0:
            f = 0
            break
        else:
            d[y] = 1
    if f == 0:
        break
if f == 1:
    print("pairwise coprime")
    exit(0)

t = A[0]
for e in A:
    t = math.gcd(e,t)

if t == 1:
    print("setwise coprime")
else:
    print("not coprime")
