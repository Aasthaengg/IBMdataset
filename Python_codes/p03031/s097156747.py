N, M = map(int, input().split())
I = []
for _ in range(M):
    I.append(list(map(int, input().split())))
p = list(map(int, input().split()))

ans = 0

for i in range(2 ** N):
    flg = 1
    for j in range(M):
        o = 0
        for k in range(1, I[j][0]+1):
            if (i >> (I[j][k]-1)) & 1:
                o += 1
        if o % 2 != p[j]:
            flg = 0
            break
    if flg == 1:
        ans += 1
print(ans)