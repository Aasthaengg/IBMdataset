# 16:00 - 16:09
N = int(input())

MAXA = 55555
P = []
X = [True]*(MAXA+1)
X[0] = X[1] = False
for i in range(MAXA+1):
    if X[i]:
        P.append(i)
        X[i::i] = [False]*(MAXA//i)
X = []
for p in P:
    if p%5==1:
        X.append(p)
print(*X[:N])