import sys
MOD = 10 ** 9 + 7
N, K = map(int, input().split())
A = list(map(int, input().split()))

X = 1

if N == K:
    for a in A:
        X = X * a % MOD
        X %= MOD
    print(X)
    sys.exit()

P = []
M = []
for a in A:
    if a >= 0:
        P.append(a)
    else:
        M.append(a)    

if len(P) == 0:
    if K % 2 != 0:
        M.sort(reverse=True)
        for i in range(K):
            X = X * M[i] % MOD
            X %= MOD
        print(X)
        sys.exit()

P.sort()
M.sort(reverse=True)

if K % 2 != 0:
    X = X * P[-1] % MOD
    X %= MOD
    K -= 1
    P.pop()

PP = []
if len(P) % 2 == 0:
    for i in range(0, len(P), 2):
        PP.append(P[i] * P[i + 1])
else:
    PP.append(P[0])
    for i in range(1, len(P), 2):
        PP.append(P[i] * P[i + 1])
if len(M) % 2 == 0:
    for i in range(0, len(M), 2):
        PP.append(M[i] * M[i + 1])
else:
    for i in range(1, len(M), 2):
        PP.append(M[i] * M[i + 1])
PP.sort(reverse=True)

i = 0
while K > 0:
    X = X * PP[i] % MOD
    X %= MOD
    K -= 2
    i += 1

print(X)