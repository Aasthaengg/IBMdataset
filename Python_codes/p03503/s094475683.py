N = int(input())
F = [list(map(int, input().split())) for _ in range(N)]
P = [list(map(int, input().split())) for _ in range(N)]
ans = -float('inf')

for i in range(2**10):
    bag = []
    for j in range(10):
        if (i>>j)&1:
            bag += [j]

    tmp = 0
    is_cnt = False
    for n in range(N):
        f = F[n]
        cnt = 0
        for b in bag:
            if f[b] == 1:
                cnt += 1
        tmp += P[n][cnt]
        if cnt:
            is_cnt = True
    
    if is_cnt:
        ans = max(ans, tmp)

print(ans)

    

        



