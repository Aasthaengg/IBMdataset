H, W = map(int,input().split())
A = []
Q = []
for _ in range(H):
    A.append(list(map(int,input().split())))
for h in range(H-1):
    for w in range(W):
        if A[h][w] % 2 == 1:
            Q.append([h+1, w+1, h+2, w+1])
            A[h+1][w] += 1
for w in range(W-1):
    if A[H-1][w] % 2 == 1:
        Q.append([H, w+1, H, w+2])
        A[H-1][w+1] += 1
print(len(Q))
for i in range(len(Q)):
    print(*Q[i])