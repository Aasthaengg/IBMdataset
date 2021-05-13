N,T = map(int,input().split())
A = list(map(int,input().split()))
B = [0 for _ in range(N)]
amax = A[-1]
for i in range(N-2,-1,-1):
    a = A[i]
    if a>amax:
        B[i] = 0
        amax = a
    else:
        B[i] = amax-a
bmax = 0
amax = 0
for i in range(N):
    b = B[i]
    if b>bmax:
        amax = A[i]+b
        bmax = b
Ind = []
for i in range(N):
    if B[i]==bmax:
        Ind.append(i)
cnt = 0
cur = N-1
for i in range(len(Ind)-1,-1,-1):
    j = Ind[i]
    amax = A[j]+B[j]
    for k in range(cur,j,-1):
        if A[k]==amax:
            cnt += 1
    cur = j
print(cnt)