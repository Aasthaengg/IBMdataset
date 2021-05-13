N = int(input())
G = [[0]*N for _ in range(N)]

for i in range(N):
    for j in range(N):
        if i!=j:
            G[i][j] = 1
            G[j][i] = 1

if N%2==0:
    for i in range(N):
        G[i][N-1-i] = 0
        
    print(N*(N-1)//2-N//2)
    
    for i in range(N):
        for j in range(i+1, N):
            if G[i][j]==1:
                print(i+1, j+1)
else:
    for i in range(N-1):
        G[i][N-2-i] = 0
        
    print(N*(N-1)//2-(N-1)//2)
    
    for i in range(N):
        for j in range(i+1, N):
            if G[i][j]==1:
                print(i+1, j+1)