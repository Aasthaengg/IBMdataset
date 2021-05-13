n,k = map(int,input().split())

if k == 0:
    G = []
    for i in range(1,n):
        for j in range(i+1,n+1):
            G.append((i,j))
    print(len(G))
    for u,v in G:
        print(u,v)
    exit(0)

if k-(n-1)*(n-2)//2 > 0:
    print(-1)
    exit(0)

G = []
for i in range(1,n):
    G.append((i,n))

count = (n-1)*(n-2)//2-k
for i in range(1,n-1):
    for j in range(i+1,n):
        if count == 0:
            print(len(G))
            for u,v in G:
                print(u,v)
            exit(0)
        G.append((i,j))
        count -= 1
