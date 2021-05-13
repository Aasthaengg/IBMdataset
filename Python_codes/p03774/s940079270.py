N,M = map(int,input().split())
A = [list(map(int,input().split())) for _ in range(N)]
B = [list(map(int,input().split())) for _ in range(M)]
B.insert(0,0)
for i in range(N):
    a,b = A[i]
    dmin = 10**9
    ind = M
    for j in range(M,0,-1):
        c,d = B[j]
        dist = abs(a-c)+abs(b-d)
        if dist<=dmin:
            dmin = dist
            ind = j
    print(ind)