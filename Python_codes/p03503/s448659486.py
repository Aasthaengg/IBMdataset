n = int(input())

opens = [list(map(int, input().split())) for _ in range(n)]

score = [list(map(int, input().split())) for _ in range(n)]

INF = 1e100
ans = -1 * INF
for i in range(2**10):
    ch = [0] * 10
    cnt = 0
    for j in range(10):
        if (i >> j) & 1:
            ch[j] = 1
            cnt += 1
    if not cnt:
        continue
    total = 0
    for k in range(n):
        ct = 0
        for l in range(10):
            if opens[k][l] and ch[l]:
                ct += 1
        total += score[k][ct]
    ans = max(ans, total)

print(ans)