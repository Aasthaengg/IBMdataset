import sys,queue,math,copy,itertools,bisect,collections,heapq
LI = lambda : [int(x) for x in sys.stdin.readline().split()]
_LI = lambda : [int(x)-1 for x in sys.stdin.readline().split()]
NI = lambda : int(sys.stdin.readline())

H,W,D = LI()
A = [_LI() for _ in range(H)]
Q = NI()
LR = [_LI() for _ in range(Q)]

dist =  [[0 for _ in range(math.ceil(H*W/D))] for _ in range(D)]
S  = []
for i in range(H):
    for j in range(W):
        S.append((A[i][j],i,j))
S.sort()

for a,i,j in S[D:]:
    dist[a%D][a//D] = dist[a%D][a//D-1] + abs(S[a-D][1]-i) + abs(S[a-D][2]-j)

for l,r in LR:
    ans = dist[r%D][r//D] - dist[l%D][l//D]
    print(ans)