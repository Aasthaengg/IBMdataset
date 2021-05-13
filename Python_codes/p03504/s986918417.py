N,C = map(int,input().split())
G = {i:[0 for _ in range(10**5+1)] for i in range(1,C+1)}
for i in range(N):
    s,t,c = map(int,input().split())
    G[c][s] += 1
    G[c][t] -= 1
F = [0 for _ in range(2*(10**5)+1)]
for c in range(1,C+1):
    for i in range(10**5+1):
        if G[c][i]==1:
            F[2*i-1] += 1
        elif G[c][i]==-1:
            F[2*i] -= 1
H = [0 for _ in range(2*(10**5)+1)]
for i in range(1,2*(10**5)+1):
    H[i] = H[i-1]+F[i]
print(max(H))