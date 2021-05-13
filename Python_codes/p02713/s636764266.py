K = int(input())
g = [[] for i in range(K+1)]
for i in range(1, K+1):
    for j in range(i, K+1, i):
        g[j].append(i)
sigma = 0
for i in range(1, K+1):
    for j in range(1, K+1):
        for k in range(1, K+1):
            for d in reversed(range(len(g[i]))):
                if g[i][d] in g[j] and g[i][d] in g[k]:
                    sigma += g[i][d]
                    break
print(sigma)