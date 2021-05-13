def gcd(a,b):
    if b==0 or a == 0  : return a + b
    return gcd(b, a%b)
N = int(input())
d1 = {}
d2 = {}
zero = 0
for _ in range(N):
    A,B = map(int, input().split())
    if A == 0 and B == 0 :
        zero += 1
        continue
    d = gcd(abs(A), abs(B))
    A,B = A//d, B//d
    if B < 0 or (B==0 and A < 0):
        A,B = -A,-B
    if A > 0 :
        if (A,B) not in d1:d1[(A,B)]=0
        d1[(A,B)]+=1
    else :
        if (A,B) not in d2:d2[(A,B)] = 0
        d2[(A,B)] += 1
ret = []
for (x,y),count in d1.items():
    if (-y, x) in d2 :
        ret.append((count, d2[(-y,x)]))
    else :
        ret.append((count, 0))
for (x,y),count in d2.items():
    if (y,-x) not in d1:
        ret.append((count, 0))
mod = 10 ** 9 + 7
ans = 1
for p,q in ret:
    if q == 0 :
        ans *= 2**p
        ans %= mod
    else :
        ans *= (2**p + 2**q -1 )
        ans %= mod
print( (ans - 1 + zero ) % mod )