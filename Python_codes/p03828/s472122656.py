from collections import defaultdict
n = int(input())
mod = 10**9 + 7
f = defaultdict(int)

def fctr1(n):
    c = 0
    r = int(n**0.5)
    for i in range(2, r+2):
        while n % i == 0:
            c += 1
            n = n//i
        if c != 0:
            f[i] += c
            c = 0
    if n != 1:
        f[n] += 1
    return f


for i in range(1, n+1):
    f = fctr1(i)

ans = 1
for v in f.values():
    ans = ans * (v+1) % mod
print(ans)



