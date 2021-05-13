S = list(input())
ls = len(S)
na = S.count("a")
nb = S.count("b")
nc = ls - na - nb
mi = min(na, nb, nc)
ma = max(na, nb, nc)

if ma - mi <= 1:
    print("YES")
else:
    print("NO")