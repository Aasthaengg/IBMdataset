N = int(input())
P = [int(input()) for i in range(N)]

D = {p:i for i,p in enumerate(P)}
pv = N
l = seq = 0
for n in range(1,N+1):
    nx = D[n]
    if pv < nx:
        seq += 1
    else:
        l = max(l,seq)
        seq = 1
    pv = nx
l = max(l, seq)

print(N - l)