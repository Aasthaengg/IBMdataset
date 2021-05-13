n = int(input())
G = []
for i in range(1, n+1):
    for j in range(i+1, n+1):
        if i+j != n+int(n%2==0):
            G.append([i, j])

print(len(G))
for g in G:
    print(*g)