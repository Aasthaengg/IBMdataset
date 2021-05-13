N, K = list(map(int, input().split()))
P = list(map(lambda x: int(x) - 1, input().split()))
C = list(map(int, input().split()))

ans = -10**9-1
for i in range(N):
    seen = [-1]*N
    cumsum = [0]*(N+1)
    now = i
    j = 0
    while seen[now] == -1:
        seen[now] = 1
        now = P[now]
        cumsum[j+1] = cumsum[j] + C[now]
        j += 1
    loop_size = j
    if K <= loop_size:
        ans = max([ans] + cumsum[1:K+1])
    else:
        if cumsum[loop_size] > 0:
            loop_n = K//loop_size - 1
            cumsum2 = cumsum[0:loop_size+1] + [x + cumsum[loop_size] for x in cumsum[1:loop_size+1]]
            score = cumsum[loop_size]*loop_n + max(cumsum2[0:loop_size+K%loop_size+1])
            ans = max(ans, score)
        else:
            ans = max([ans] + cumsum[1:loop_size+1])
print(ans)