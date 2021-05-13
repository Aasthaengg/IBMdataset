N = int(input())

cnt = 0
G = [[] for i in range(N + 1)]
for i in range(1, N + 1):
    for j in range(i, N + 1):
        if N % 2 == 1:
            if i + j != N and i != j:
                G[i].append(j)
                cnt += 1
        else:
            if i + j != N + 1 and i != j:
                G[i].append(j)
                cnt += 1

print(cnt)

for i in range(1, N + 1):
    for g in G[i]:
        print(i, g)