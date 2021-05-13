N = int(input())
F = [list(map(int,input().split())) for i in range(N)]
P = [list(map(int,input().split())) for i in range(N)]

import itertools

ans = -10**10
for I in itertools.product([0,1],repeat=10):
    if sum(list(I))==0:
        continue
    
    TMP = 0
    for i in range(N):
        tmp = 0
        for j in range(10):
            if F[i][j]==1 and I[j]==1:
                tmp+=1
        TMP += P[i][tmp]
    
    ans = max(ans,TMP)

print(ans)
         
