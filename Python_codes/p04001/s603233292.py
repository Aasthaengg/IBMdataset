S = list(input())
N = len(S)

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
    A = list(map(int,T.split("+")))
    out += sum(A)
print(out)