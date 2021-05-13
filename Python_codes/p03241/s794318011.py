import math
N, M = map(int,input().split())
b = 0

P = [1]
for k in range(2,math.floor(math.sqrt(M))+1):
    if M % k == 0:
        P.append(k)
        P.append(M//k)

P = sorted(P)
for e in P:
    if e >= N:
        print(M//e)
        exit(0)
print(1)
