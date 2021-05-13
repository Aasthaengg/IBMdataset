S = list(input())
N = len(S)
D = {}
for i in range(N):
    D[S[i]] = D.get(S[i],[-1])
    D[S[i]].append(i)
out = 100
for L in D.values():
    L.append(N)
    LN = len(L)
    tmp = 0
    for i in range(LN-1):
        tmp = max(tmp, L[i+1]-L[i]-1)
    out=min(out,tmp)
print(out)
