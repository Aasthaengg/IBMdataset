N = int(input())

if N % 2 == 0:
    G = []
    G_append = G.append
    for i in range(1, N):
        for j in range(i + 1, N + 1):
            if i + j != (1 + N):
                G_append((i, j))
    print (len(G))
    for g in G:
        print (*g, sep = ' ')
    
else:
    G = []
    G_append = G.append
    for i in range(1, N):
        for j in range(i + 1, N + 1):
            if i + j != N:
                G_append((i, j))
    print (len(G))
    for g in G:
        print (*g, sep = ' ')


