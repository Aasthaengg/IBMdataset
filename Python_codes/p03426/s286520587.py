H,W,D = map(int,input().split())
A = [list(map(int,input().split())) for _ in range(H)]
Q = int(input())
px = [0]*(H*W+1)
py = [0]*(H*W+1)
for y in range(H):
    for x in range(W):
        n = A[y][x]
        px[n] = x + 1
        py[n] = y + 1
csum = [0]*(H*W+1)
for i in range(D+1,H*W+1):
    csum[i] = csum[i-D] + abs(px[i]-px[i-D]) + abs(py[i]-py[i-D])
for q in range(Q):
    L, R = map(int,input().split())
    print(csum[R]-csum[L])

