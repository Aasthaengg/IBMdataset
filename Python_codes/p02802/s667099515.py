N, M = map(int, input().split())
ps = [list(map(str, input().split())) for _ in range(M)]
ans = [0,0]
cnt = [0]*(N+1)
memo = [0]*(N+1)
for i in range(M):
    p = int(ps[i][0])
    s = ps[i][1]
    if memo[p] == 1:
        continue
    else:
        if s == "WA":
            ans[1] += 1
            cnt[p] += 1
        else:
            ans[0] += 1
            cnt[p] += 1
            memo[p] = 1

for i in range(1,N+1):
    if memo[i] == 0:
        ans[1] -= cnt[i]
        
print(*ans)