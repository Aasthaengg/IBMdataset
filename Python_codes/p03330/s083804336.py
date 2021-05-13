import sys,queue,math,copy,itertools,bisect,collections,heapq
INF = 10**18
LI = lambda : [int(x) for x in sys.stdin.readline().split()]

N,C = LI()
D = [LI() for _ in range(C)]
p = [LI() for _ in range(N)]
q = [[0] * (C+1) for _ in range(3)]
for i in range(N):
    for j in range(N):
        k = (i + j) % 3
        q[k][p[i][j]] += 1

ans = INF
for col in itertools.permutations(range(1,C+1),3):
    iwa = 0
    for i in range(3):
        for j in range(1,C+1):
            iwa += D[j-1][col[i]-1] * q[i][j]
    ans = min(ans,iwa)
print (ans)
