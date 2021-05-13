from collections import Counter

N = int(input())
P = []
for _ in range(N):
    P.append(int(input()))

G = [0] * (N+1)
id = 1

for i in range(N):
    if G[P[i]-1] != 0:
        G[P[i]] = G[P[i]-1]
    else:
        G[P[i]] = id
        id+=1

C = Counter(G)

m = max(C.values())

print(N - m)


