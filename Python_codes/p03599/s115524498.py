def calcCons(nA, nB, nC, nD):
    W = (nA * a + nB * b) * 100
    S = nC * c + nD * d
    if W + S == 0:
        return -1
    return S / (W + S)


a, b, c, d, e, f = map(int, input().split())
nA, nB, nC, nD, W, S, M = 0, 0, 0, 0, 0, 0, 0
while nA * a * 100 + nB * b * 100 + nC * c + nD * d <= f:
    while nA * a * 100 + nB * b * 100 + nC * c + nD * d <= f:
        while nA * a * 100 + nB * b * 100 + nC * c + nD * d <= f:
            while nA * a * 100 + nB * b * 100 + nC * c + nD * d <= f:
                cons = calcCons(nA, nB, nC, nD)
                if cons > M and cons <= e / (100 + e):
                    M = cons
                    W, S = nA * a * 100 + nB * b * 100, nC * c + nD * d
                nD += 1
            nD = 0
            nC += 1
        nC = 0
        nB += 1
    nB = 0
    nA += 1

if M == 0:
    W = a * 100
print(W + S, S)
