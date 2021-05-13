import math
def divs(n):
    res = []
    for i in range(1, n+1):
        if i * i > n:
            break
        if n % i == 0:
            res.append(i)
            if i != n//i:
                res.append(n//i)
    return res

def one(n, k):
    if k == 1:
        return False
    while n % k == 0:
        n //= k
    n %= k
    return n == 1


n = int(input())

ans = sorted(set(divs(n) + divs(n-1)))

ok = 0
for x in ans:
    if one(n, x):
        ok += 1

print(ok)
