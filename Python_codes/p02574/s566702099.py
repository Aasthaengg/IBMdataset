# E - Coprime
from math import gcd

N = int(input())
A = list(map(int,input().split()))
MAX = 10**6
p = [0]*(MAX+1)

for i in range(2,MAX+1):
    if p[i]>0:
        continue
    tmp = i
    while tmp<=MAX:
        p[tmp] = i
        tmp += i

pairwise = True
g = -1
q = [N]*(MAX+1)

for i in range(N):
    a = A[i]
    g = a if g<0 else gcd(g,a)
    while pairwise and a>1:
        pairwise = False if q[p[a]]<i else True
        q[p[a]] = i
        a //= p[a]

if pairwise:
    print('pairwise coprime')
elif g==1:
    print('setwise coprime')
else:
    print('not coprime')