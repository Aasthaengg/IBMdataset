MOD = 10**9 + 7
S = input()

l = len(S)
nAB = [0]*(l+1)
nA = [0]*(l+1)
nB = [0]*(l+1)
nC = [0]*(l+1)
nABC = [0]*(l+1)

add = 1
for i,s in enumerate(S):
    if s == '?':
        nA[i+1] = 3*nA[i] + add
        nB[i+1] = 3*nB[i] + add
        nC[i+1] = 3*nC[i] + add
        nAB[i+1] = 3*nAB[i] + nA[i]
        nABC[i+1] = 3*nABC[i] + nAB[i]
        add = (add * 3) % MOD
    if s == 'A':
        nA[i+1] = nA[i] + add
        nB[i+1] = nB[i]
        nC[i+1] = nC[i]
        nAB[i+1] = nAB[i]
        nABC[i+1] = nABC[i]
    if s == 'B':
        nA[i+1] = nA[i]
        nB[i+1] = nB[i] + add
        nC[i+1] = nC[i]
        nAB[i+1] = nAB[i] + nA[i]
        nABC[i+1] = nABC[i]
    if s == 'C':
        nA[i+1] = nA[i]
        nB[i+1] = nB[i]
        nC[i+1] = nC[i] + add
        nAB[i+1] = nAB[i]
        nABC[i+1] = nABC[i] + nAB[i]
    nA[i+1] = nA[i+1] % MOD
    nB[i+1] = nB[i+1] % MOD
    nC[i+1] = nC[i+1] % MOD
    nAB[i+1] = nAB[i+1] % MOD
    nABC[i+1] = nABC[i+1] % MOD

print(nABC[l] % MOD)

