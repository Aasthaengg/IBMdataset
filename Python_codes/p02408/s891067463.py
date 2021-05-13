S = []
H = []
C = []
D = []
for i in (S, H, C, D):
        for k in range(1, 13+1):
            i.append(k)


for u in range(0, int(input())):
    x, y = (i for i in input().split())
    if x == "S":
        S.remove(int(y))
    elif x == "H":
        H.remove(int(y))
    elif x == "C":
        C.remove(int(y))
    else:
        D.remove(int(y))
if len(S) > 0:
    for s in range(0, len(S)):
        print("S",S[s])
if len(H) > 0:
    for h in range(0, len(H)):
        print("H",H[h])
if len(C) > 0:
    for c in range(0, len(C)):
        print("C",C[c])
if len(D) > 0:
    for d in range(0, len(D)):
        print("D",D[d])