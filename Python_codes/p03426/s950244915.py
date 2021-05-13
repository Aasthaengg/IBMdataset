from math import ceil

H, W, D = [int(i) for i in input().split()]
N = H*W
A = [[int(i) for i in input().split()] for _ in range(H)]

M = [0] * (N+1)
for h in range(H):
    for w in range(W):
        M[A[h][w]] = (h, w)

def f(s, t):
    if s==0: return 0
    return abs(s[0]-t[0])+abs(s[1]-t[1])


cumsum = [[0] for _ in range(D)]
for s in range(1, D+1):
    for i in range(s, N+1, D):
        if i <= D: cumsum[s-1].append(0)
        else: cumsum[s-1].append(cumsum[s-1][-1]+f(M[i-D], M[i]))

Q = int(input())
for _ in range(Q):
    L, R = [int(i) for i in input().split()]
    i = (L%D)-1
    if i==-1:
        print(cumsum[i][R//D] - cumsum[i][L//D])
    else:
        print(cumsum[i][ceil(R/D)] - cumsum[i][ceil(L/D)])