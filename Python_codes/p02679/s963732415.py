n = int(input())
ab = []
for _ in range(n):
    a, b = map(int, input().split())
    ab.append((a, b))
di = {}
z = 0
def gcd(a, b):
    while b!=0:
        a, b = b, a%b
    return a
for a, b in ab:
    if a*b!=0:
        g = gcd(abs(a), abs(b))
        a, b = a//g, b//g
    if a*b>0:
        ind = (abs(a), abs(b))
    elif a*b<0:
        ind = (abs(b), abs(a))
    else:
        ind = 0
    if ind in di:
        x, y = di[ind]
    else:
        x = y = 0
    if a*b==0:
        if b!=0:
            di[ind] = (x+1, y)
        elif a!=0:
            di[ind] = (x, y+1)
        else:
            z += 1
    else:
        if a*b>0:
            di[ind] = (x+1, y)
        else:
            di[ind] = (x, y+1)
mod = 10**9+7
ans = 1
for i, j in di.values():
    ans *= (pow(2, i, mod)+pow(2, j, mod)-1)
    ans %= mod
print((ans+z-1)%mod)