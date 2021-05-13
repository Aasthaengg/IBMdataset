N = int(input())
L = [list(map(int,input().split())) for k in range(N-1)]
c = sorted(list(map(int,input().split())))
a = sum(c) - c[-1]
T = [[] for k in range(N)]
for e in L:
    T[e[0]-1].append(e[1]-1)
    T[e[1]-1].append(e[0]-1)

kyori = [-1 for k in range(N)]
que = [L[0][0]]
kyori[L[0][0]] = c.pop()

while len(que) > 0:
    now = que.pop()
    for tsugi in T[now]:
        if kyori[tsugi] == -1:
            kyori[tsugi] = c.pop()
            que.append(tsugi)
print(a)
print(*kyori, sep=" ")
