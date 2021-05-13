from collections import Counter
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

m = int(input())
a = Counter()

for i in range(2,m+1):
    a += Counter(pf(i))

ans = 1
for i in range(1,1001):
    if a[i] == 0:
        continue
    else:
        ans = ans * (a[i] + 1) % div
        
print(ans)