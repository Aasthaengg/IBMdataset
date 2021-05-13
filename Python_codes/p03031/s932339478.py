n, m = map(int, input().split())
ks = [list(map(int, input().split())) for _ in range(m)]
p = list(map(int, input().split()))

ans = 0
for i in range(2**n):
    flag = True
    for j in range(m):
        cnt = 0
        for k in range(1, len(ks[j])):
            if (i >> (ks[j][k]-1)) & 1:
                cnt += 1
        if cnt % 2 != p[j]:
            flag = False
            break
    if flag:
        ans += 1
print(ans)