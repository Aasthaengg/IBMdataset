n = int(input())
a = list(map(int,input().split()))
mod = 10**9 + 7
r = 0
b = 0
g = 0
ans = 1
for i in range(n):
    p = 0
    if a[i] == r:
        p += 1
        r += 1
    if a[i] == b:
        p += 1
        if p == 1:
            b += 1
    if a[i] == g:
        p += 1
        if p == 1:
            g += 1
    ans *= p
    ans %= mod
print(ans)