N = int(input())

G = []

for i in range(N):
    s,p = input().split()
    g = [s] + [100 - int(p)] + [i + 1]
    G.append(g)

G = sorted(G)

for i in range(N):
    print(G[i][2])