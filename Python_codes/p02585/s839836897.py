N, K = map(int,input().split())
P = list(map(int,input().split()))
C = list(map(int,input().split()))

ans = -10**18
for start in range(N):
    now = start
    cycle = [0]

    while True:
        now = P[now] - 1
        cycle.append(cycle[-1] + C[now])

        if now == start: break

    L = len(cycle)-1
    if cycle[-1] < 0 or K <= L:
        score = max(cycle[1:min(L+1,K)+1])
    else:
        score1 = cycle[-1]*(K//L) + max(cycle[:K%L+1])
        score2 = cycle[-1]*(K//L-1) + max(cycle)
        score = max(score1, score2)

    ans = max(ans, score)

print(ans)