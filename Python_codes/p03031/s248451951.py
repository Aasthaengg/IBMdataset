N, M = map(int, input().split())
ks = [list(map(int, input().split())) for _ in range(M)]
p = list(map(int, input().split()))

ans = 0
for ii in range(2**N):
    check = True
    for i in range(M):
        cnt = 0
        for j in range(1, len(ks[i])):
            if (ii >> (ks[i][j]-1)) & 1:
                cnt += 1
        if cnt % 2 != p[i]:
            check = False
            break
    if check:
        ans += 1
print(ans)