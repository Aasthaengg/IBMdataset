N,M = list(map(int,input().split()))
P = [[] for i in range(N)]
for i in range(N):
    X,Y,Z = list(map(int,input().split()))
    P[i].append( X+Y+Z)
    P[i].append( X+Y-Z)
    P[i].append( X-Y+Z)
    P[i].append( X-Y-Z)
    P[i].append(-X+Y+Z)
    P[i].append(-X+Y-Z)
    P[i].append(-X-Y+Z)
    P[i].append(-X-Y-Z)

out = 0
for i in range(8):
    P.sort(key=lambda x:x[i],reverse=True)
    S = 0
    for j in range(M):
        S+=P[j][i]
    if S>out:
        out = S
print(out)
