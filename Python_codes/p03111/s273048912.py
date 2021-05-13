from itertools import permutations,product
N,A,B,C = map(int,input().split())
L = [int(input()) for _ in range(N)]
G = {0:[],1:[],2:[]}
cmin = 10**5
for x in permutations(range(N),3):
    for y in product(range(4),repeat=N-3):
        G[0] = [x[0]]
        G[1] = [x[1]]
        G[2] = [x[2]]
        G[3] = []
        Ind = list(range(N))
        Ind.remove(x[0])
        Ind.remove(x[1])
        Ind.remove(x[2])
        for i in range(N-3):
            G[y[i]].append(Ind[i])
        cA = 0
        nA = len(G[0])
        cA = (nA-1)*10
        xA = 0
        for j in range(nA):
            xA += L[G[0][j]]
        cA += abs(A-xA)
        cB = 0
        nB = len(G[1])
        cB = (nB-1)*10
        xB = 0
        for j in range(nB):
            xB += L[G[1][j]]
        cB += abs(B-xB)
        cC = 0
        nC = len(G[2])
        cC = (nC-1)*10
        xC = 0
        for j in range(nC):
            xC += L[G[2][j]]
        cC += abs(C-xC)
        cmin = min(cmin,cA+cB+cC)
print(cmin)