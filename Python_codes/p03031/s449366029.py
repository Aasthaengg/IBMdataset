N,M = map(int,input().split())
k = [list(map(int,input().split()))for _ in range(M)]
p = list(map(int,input().split()))
ans = 0
for S in range(1 << N):
    res = [pp==0 for pp in p]
    for j in range(N):
        if (S >> j) & 1:
            for l in range(M):
                if j+1 in k[l][1:]:
                    res[l] = not res[l]
    if res == [True] * M:
        ans += 1
print(ans)
