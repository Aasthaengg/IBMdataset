from bisect import *
S = input()
mod = 10**9 + 7
A = []
B = []
C = []
X = []
q = 0
for i,s in enumerate(S):
    if s == 'A':
        A.append(i)
    elif s == 'B':
        B.append((i,0))
    elif s == 'C':
        C.append(i)
    else:
        X.append(i)
        B.append((i,1))
        q += 1

pow3 = [pow(3,q,mod),pow(3,max(0,q-1),mod),pow(3,max(0,q-2),mod),pow(3,max(0,q-3),mod)]
ans = 0
for b,flag in B:
    Al = bisect_left(A,b)
    Cr = (len(C) - bisect_right(C,b))
    Xl = bisect_left(X,b)
    Xr = (len(X) - bisect_right(X,b))
    ans += (Al*Cr%mod)*pow3[flag]%mod
    ans %= mod
    ans += (Al*Xr%mod + Xl*Cr%mod)*pow3[flag+1]%mod
    ans %= mod
    ans += (Xl*Xr%mod)*pow3[flag+2]%mod
print(ans)
