n = int(input())
pos = []
for _ in range(n):
    p = list(map(int, input().split()))
    pos.append(p)

ans = 0
for i in range(n):
    for j in range(n):
        if i == j:
            continue
        dpos = [pos[i][0] - pos[j][0], pos[i][1] - pos[j][1]]
        cnt = 0
        for k in range(n):
            for l in range(n):
                if k == l:
                    continue
                tmp = [pos[k][0] - pos[l][0], pos[k][1] - pos[l][1]]
                if dpos[0] == tmp[0] and dpos[1] == tmp[1]:
                    cnt += 1
        ans = max(cnt, ans)

print(n-ans)
