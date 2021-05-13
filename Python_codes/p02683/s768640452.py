from itertools import product
N,M,X = map(int,input().split())
A = [list(map(int,input().split())) for _ in range(N)]
C = []
for i in range(N):
    C.append(A[i].pop(0))
ans = sum(C)+10
for x in product((0,1),repeat=N):
    flag = 0
    for j in range(M):
        cnt = 0
        for i in range(N):
            if x[i]==1:
                cnt += A[i][j]
        if cnt<X:
            flag = 1
            break
    if flag==0:
        tot = 0
        for i in range(N):
            if x[i]==1:
                tot += C[i]
        ans = min(ans,tot)
if ans>sum(C):
    print(-1)
else:
    print(ans)