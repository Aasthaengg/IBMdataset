H,W,D = map(int,(input().split()))

A = [[] for _ in range(H)]
for i in range(H):
    A[i] = list(map(int,(input().split())))

d = {}
for i in range(H):
    for j in range(W):
        d[A[i][j]] = (i,j)

s = [[] for _ in range(D+1)]
for i in range(1,D+1):
    cost = 0
    s[i].append(0)
    for j in range(i,H*W-D+1,D):
        cost += abs(d[j][0] - d[j+D][0]) + abs(d[j][1] - d[j+D][1])
        s[i].append(cost)

Q = int(input())
for i in range(Q):
    L,R = map(int,(input().split()))
    r = L%D
    if r == 0:
        r = D
    ans = s[r][(R-r)//D]-s[r][(L-r)//D]
    print(ans)