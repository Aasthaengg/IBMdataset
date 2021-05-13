# ABC 136 E
import math

N, K = map(int,input().split())
A = list(map(int,input().split()))
S = sum(A)

P = [1,S]
for k in range(2,math.floor(math.sqrt(S))+1):
    if S % k == 0:
        P.append(k)
        P.append(S//k)
P = sorted(P)[::-1]

for e in P:
    t = []
    u = []
    for a in A:
        if a%e != 0:
            t.append(a%e)
            u.append(e-a%e)
    t = sorted(t)
    if len(t) == 0:
        print(e)
        exit(0)
    else:
        p = [f for f in t]
        for k in range(1,len(t)):
            p[k] += p[k-1]
        m = [e-f for f in t]
        for k in range(1,len(t)):
            m[-k-1] += m[-k]
        for k in range(len(t)-1):
            if p[k] == m[k+1] and p[k] <= K:
                print(e)
                exit(0)
