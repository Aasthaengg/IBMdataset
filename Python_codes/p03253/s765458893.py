from math import sqrt,ceil
N,M=map(int,input().split())
l=[]
for i in range(2,ceil(sqrt(M))):
    t=0
    while not M%i:
        M//=i
        t+=1
    if t:
        l.append(t)
if M>1:
    l.append(1)
MAX_NUM = 10**5 + 100
pr = 10**9+7
fac  = [0 for _ in range(MAX_NUM)]
finv = [0 for _ in range(MAX_NUM)]
inv  = [0 for _ in range(MAX_NUM)]
fac[0]  = fac[1] = 1
finv[0] = finv[1] = 1
inv[1] = 1
for i in range(2,MAX_NUM):
    fac[i] = fac[i-1] * i % pr
    inv[i] = pr - inv[pr%i] * (pr // i) % pr
    finv[i] = finv[i-1] * inv[i] % pr
def c(n,k):
    if n < k:
        return 0
    if n < 0 or k < 0:
        return 0
    return fac[n] * (finv[k] * finv[n-k] % pr) % pr
a=1
for i in l:
    a=a*c(N+i-1,i)%pr
print(a)