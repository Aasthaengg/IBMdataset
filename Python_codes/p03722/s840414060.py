from collections import deque


N,M = map(int,input().split())

dic = {}

for i in range(M):

    a,b,c = map(int,input().split())

    a -= 1
    b -= 1

    if a not in dic:
        dic[a] = []

    dic[a].append([b,c])

lis = [[0] * N for j in range(N)]
lis[0][0] = 1
lmax = [0] * N
lmax[0] = 1

mcost = [-1 * float("inf")] * N
mcost[0] = 0

q = deque([])
q.append(0)
cnt = 0

while len(q) > 0:

    now = q.pop()

    if now not in dic or lmax[now] > N:
        continue

    for npath in dic[now]:

        b = npath[0]
        c = npath[1]

        if mcost[now] + c > mcost[b]:
            mcost[b] = mcost[now] + c
            lis[b] = lis[now].copy()
            lmax[b] = lmax[now]
            lis[b][b] += 1
            lmax[b] = max(lmax[b],lis[b][b])

            if lmax[b] >= 2:
                mcost[b] = float("inf")
            q.append(b)

    if lis[N-1][N-1] != -1 * float("inf") and lmax[N-1] >= 2:
        mcost[N-1] = float("inf")
        break

    elif mcost[N-1] == float("inf"):
        break

print (mcost[N-1])
