N, M, X = map(int, input().split())
CA = [list(map(int, input().split())) for i in range(N)]
ans = -1
for i in range(1 << N):
    rikai = [0]*M
    buy = 0
    ok=1
    for j in range(N):
        if (i >> j) & 1:
            for k in range(M):
                rikai[k] += CA[j-1][k+1]
            buy += CA[j-1][0]
    for a in rikai:
        if a >= X:
            continue
        else:
            ok=0
            break
    if ok==1:
        if ans == -1:
            ans = buy
        else:
            ans = min(ans, buy)
print(ans)
