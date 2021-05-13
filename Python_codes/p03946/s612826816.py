N,T = map(int,input().split())
A = list(map(int,input().split()))
B = [(0,-1) for _ in range(N)]
amax = A[-1]
ind = N-1
bmax = 0
for i in range(N-2,-1,-1):
    a = A[i]
    if a>amax:
        amax = a
        ind = i
    else:
        B[i] = (amax-a,ind)
        if bmax<amax-a:
            bmax = amax-a
C = []
for i in range(N):
    if B[i][0]==bmax:
        if B[i][1] not in C:
            C.append(B[i][1])
print(len(C))