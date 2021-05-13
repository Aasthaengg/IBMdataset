from itertools import groupby
MOD = 10**9+7
input()
S = input()
T = input()
def f(s): return list(map(lambda p: len(list(p[1])), groupby(s)))
A = f(f(S))
p2 = 0
p3 = 1
if len(A) > 1:
    Av = A[S[0]!=T[0]::2]
    Ah = A[S[0]==T[0]::2]
    p2 += sum(Av)-len(Av)+len(Ah)
    p3 += sum(Ah)-len(Ah)
elif S[0]==T[0]:
    Av = A[S[0]!=T[0]::2]
    p2 += sum(Av)-len(Av)
else:
    Ah = A[S[0]==T[0]::2]
    p3 += sum(Ah)-len(Ah)
    p2 += len(Ah)
print(pow(2,p2,MOD)*pow(3,p3,MOD)%MOD)