import sys
input = sys.stdin.readline
from math import gcd

N = int(input())
A = list(map(int, input().split()))
era = [-1]*(10**6+1)

for i in range(2, 10**6+1):
    if era[i]==-1:
        era[i] = i

        for j in range(2*i, 10**6+1, i):
            if era[j]==-1:
                era[j] = i

s = set()
flag = True

for Ai in A:
    f = []
    t = Ai
    
    while t>1:
        f.append(era[t])
        t //= era[t]
    
    for fi in f:
        if fi in s:
            flag = False
    
    for fi in f:
        s.add(fi)

if flag:
    print('pairwise coprime')
    exit()

G = 0

for Ai in A:
    G = gcd(G, Ai)

if G==1:
    print('setwise coprime')
else:
    print('not coprime')