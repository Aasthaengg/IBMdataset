from scipy.spatial.distance import cityblock

N,M = [int(i) for i in input().split()]
S = [[int(i) for i in input().split()] for _ in range(N)]
C = [[int(i) for i in input().split()] for _ in range(M)]
d = [0]*M

for i in range(N):
    for j in range(M):
        d[j] = cityblock(S[i],C[j])
    print(d.index(min(d))+1)
