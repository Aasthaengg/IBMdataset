N, M = map(int, input().split())
D = [[] for _ in range(N)]
R = [0]*M
for i in range(M):
    P, Y = map(int, input().split())
    D[P-1].append((Y,i))
for P in range(N):
    for k, p in enumerate(sorted(D[P])):
        Y, i = p
        R[i] = (P+1)*10**6+(k+1)
for r in R:
    print("{:012}".format(r))