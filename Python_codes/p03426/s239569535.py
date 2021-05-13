h, w, d = map(int, input().split())
A = []
for _ in range(h):
    a = list(map(int, input().split()))
    A.append(a)

q = int(input())
LR = []
for _ in range(q):
    l, r = map(int, input().split())
    LR.append([l,r])

Inds = {x:[] for x in range(1, h*w+1)}
for j in range(h):
    for k in range(w):
        Inds[A[j][k]].append(j)
        Inds[A[j][k]].append(k)

Dist = [-1 for _ in range(h*w+1)]
for i in range(1,h*w+1):
    if i <= d:
        Dist[i] = 0
    else:
        Dist[i] = Dist[i-d] + abs(Inds[i][0]-Inds[i-d][0]) + abs(Inds[i][1]-Inds[i-d][1])

for lr in LR:
    ans = Dist[lr[1]] - Dist[lr[0]]
    print(ans)