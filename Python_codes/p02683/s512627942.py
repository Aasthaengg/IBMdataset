N, M, X = map(int, input().split())
a = [list(map(int, input().split())) for l in range(N)]
 
ans = 10**8
 
for i in range(2**N):
    score = [0] * M
    total = 0
    for j in range(N):
        if ((i >> j) & 1):
            total += a[j][0]
            for k in range(M):
                score[k] += a[j][k+1]
        
    if min(score) >= X:
        ans = min(ans, total)
 
if ans == 10**8:
    print(-1)
else:
    print(ans)