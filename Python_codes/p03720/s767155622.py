N,M = map(int,input().split())
C = [0]*N
R = [list(map(int,input().split())) for _ in range(M)]
for a,b in R:
    C[a-1] += 1
    C[b-1] += 1
for c in C:
    print(c)