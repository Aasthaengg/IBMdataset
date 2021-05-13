S = list(input())
N = len(S)

def calc(T):
    N = len(T)
    t = 0
    ans = 0
    tmp = 0
    while T[t]!="=":
        if T[t]=="+":
            ans += tmp
            tmp = 0
            t+=1
            continue
        else:
            tmp = 10*tmp+int(T[t])
            t+=1
    ans += tmp
    return ans

from itertools import product
LS = list(product([0,1], repeat=N-1))
out = 0
for L in LS:
    T = S[0]
    for i in range(N-1):
        if L[i]==1:
            T += "+"+S[i+1]
        else:
            T += S[i+1]
    T += "="
    out += calc(T)
print(out)