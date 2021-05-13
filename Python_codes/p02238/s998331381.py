n = int(input())
G = [[] for _ in range(n)]
u1 = 0
for _ in range(n):
    u, k, *v = [int(i) for i in input().split()]
    G[u - 1] = v
    if k != 0 and u1 == 0:
        u1 = u

time = 1
u = u1
D = []
out = [[i+1, 0, 0] for i in range(n)]
T = []
while True:
    if u not in D:
        out[u - 1][1] = time
        D.append(u)
        T.append(u)

    for d in D:
        if d in G[u - 1]:
            idx = G[u - 1].index(d)
            del G[u - 1][idx]

    if G[u - 1] == []:
        time += 1
        out[T.pop() - 1][2] = time
        if T == []:
            if len(D) == n:
                break
            else:
                for ni in range(n):
                    if ni + 1 not in D:
                        u = ni + 1
                        break
                time += 1
                continue
        else:
            u = T[-1]
    else:
        u = G[u - 1].pop(0)
        time += 1

for ni in range(n):
    print(*out[ni])

