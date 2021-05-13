from collections import Counter
import math
div = 10**9 + 7

def pf(n):
    a = []
    while n % 2 == 0:
        a.append(2)
        n //= 2
    f = 3
    while f * f <= n:
        if n % f == 0:
            a.append(f)
            n //= f
        else:
            f += 2
    if n != 1:
        a.append(n)
    return a

n , m = map(int,input().split())
a = Counter(pf(m))

ans = 1
for i in a:
    temp = math.factorial(a[i] + n - 1 ) // ( math.factorial(a[i]) * math.factorial(n-1) )
    ans = ans * temp % div
    
print(ans)