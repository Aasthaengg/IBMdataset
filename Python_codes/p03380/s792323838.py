def pow(x, n , mod):
    res = 1
    while n > 0:
        if  bin(n & 1) == bin(1) :
            res = res * x % mod
        x = x*x % mod
        n = n >>1
    return res   

def combination(n,a):
    x = 1
    for i in range(a):
        x = x * (n-i) % mod
    y = 1
    for i in range(a):
        y = y * (a-i) % mod
    y = pow(y, mod-2, mod)
    return (x*y % mod)

n = int(input())
a = list(map(int, input().split()))
mod =1

m = max(a)
a = sorted(a)

ans = 0

for i in a:
    if abs(m/2-i) < abs(m/2-ans):
        ans = i

print(m, ans)