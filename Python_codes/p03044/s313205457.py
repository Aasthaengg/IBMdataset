N = int(input())
D = {i: [] for i in range(N)}
distD = {}
for i in range(N-1):
    u, v, w = map(int, input().split())
    u -= 1
    v -= 1
    D[u].append(v)
    D[v].append(u)
    distD[u*N+v], distD[v*N+u] = w, w
clr = [-1 for _ in range(N)]
clr[0] = 0
s = [0]
pnt = 0
cnt = 1
while pnt < cnt:
    n = cnt
    for i in range(pnt, cnt):
        L = D[s[i]]
        for j in L:
            if clr[j] == -1:
                clr[j] = (clr[s[i]] + distD[s[i]*N+j]) % 2
                s.append(j)
                cnt += 1
    pnt = n
for i in range(N):
    print(clr[i])