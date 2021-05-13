G = [[] for _ in range(4)]
for _ in range(3):
    a, b = map(int,input().split())
    a -= 1
    b -= 1
    G[a].append(b)
    G[b].append(a)

for i in range(4):
    for j in range(4):
        for k in range(4):
            for l in range(4):
                if i != j and j != k and k != l and l != i and i != k and j != l:
                    if j in G[i] and k in G[j] and l in G[k]:
                        print("YES")
                        exit()
print("NO")