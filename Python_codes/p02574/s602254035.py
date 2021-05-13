import math

N = int(input())
A = list(map(int,input().split()))

A_max = max(A)

D = [i for i in range(1+A_max)]

for i in range(2,1+int(A_max**(1/2))):
    if D[i] == i:
        for j in range(2,1+A_max//i):
            D[i*j] = i

prime = {}

for i in range(2,1+A_max):
    if D[i] == i:
        prime[i] = 0

for a in A:
    X = []
    aa = a
    while aa > 1:
        X.append(D[aa])
        aa //= D[aa]
    
    X = set(X)

    for x in X:
        prime[x] += 1

if all([v<=1 for v in prime.values()]):
    print('pairwise coprime')

else:
    g = A[0]
    for i in range(1,N):
        g = math.gcd(g,A[i])
    if g == 1:
        print('setwise coprime')
    else:
        print('not coprime')