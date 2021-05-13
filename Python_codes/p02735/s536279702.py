H, W = [int(x) for x in input().split()]

S = []
S.append('.'*105)
for h in range(H):
    r = input()
    S.append('-' + r)

A = [[float("INF")] * 105 for _ in range(105)]
A[1][1] = (1 if S[1][1] == '#' else 0)


for h in range(1,H+1):
    for w in range(1,W+1):
        a = A[h][w]
        if S[h][w] == '#':
            if S[h][w-1] == '#':
                a = min(a, A[h][w-1])
            else:
                a = min(a, A[h][w-1] + 1)
            if S[h-1][w] == '#':
                a = min(a, A[h-1][w])
            else:
                a = min(a, A[h-1][w] + 1)
            A[h][w] = a
        else:
            A[h][w] = min(A[h][w-1], A[h-1][w], A[h][w])
            
print(A[H][W])
