import math
def comb(n, r): #comb(int, int)
    return math.factorial(n) // (math.factorial(n - r) * math.factorial(r))
n,p = map(int,input().split())
a = list(map(int,input().split()))
a_even = 0
a_odd = 0
for i in range(n):
    if a[i]%2 == 0:
        a_even += 1
    else:
        a_odd += 1
ans = 0
if p%2 == 0:
    k = 0
    for i in range(10**10):
        if 2*i > a_odd:
            break
        k += comb(a_odd, 2*i)
    print(k*2**a_even)
else:
    k = 0
    for i in range(10**10):
        if 2*i+1 > a_odd:
            break
        k += comb(a_odd, 2*i+1)
    print(k*2**a_even)