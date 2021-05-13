N , M = map(int,input().split())
C = list(map(int,input().split()))

G = [[0]*(N+1) for _ in range(M+1)]

for i in range(N+1):
    G[0][i] = 1000000

for kinds in range(1,M+1):
    for kingaku in range(1,N+1):
        if kingaku-C[kinds-1]<0:
            G[kinds][kingaku] = G[kinds-1][kingaku]
            continue
        #print('\n')
        #print(f'kingaku:{kingaku}, kinds:{kinds}')
        #print(G[kinds-1][kingaku])
        #print(G[kinds][kingaku-C[kinds-1]]+1)
        G[kinds][kingaku] = min(G[kinds-1][kingaku], G[kinds][kingaku-C[kinds-1]]+1)
        #print(f'index{kinds},{kingaku}')
        #print(G[kinds][kingaku])

#print(G)
print(G[M][N])


