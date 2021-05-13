H, W, D = map(int, input().split())
A = []
for i in range(H):
    A.append(list(map(int, input().split())))

num = [() for _ in range(H*W+1)]
for i in range(H):
    for j in range(W):
        num[A[i][j]] = (i,j)
wa = [0]*(H*W+1)
for i in range(D+1, H*W+1):
    wa[i] = wa[i-D] + abs(num[i][0]-num[i-D][0])+abs(num[i][1]-num[i-D][1])

Q = int(input())
for i in range(Q):
    l, r = map(int, input().split())
    print(wa[r]-wa[l])
