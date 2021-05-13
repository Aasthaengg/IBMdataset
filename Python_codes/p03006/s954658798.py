N = int(input())
coord = []
for _ in range(N):
    x, y = map(int, input().split(" "))
    coord.append((x, y))

ans = N

for k in range(N):
    for l in range(N):
        if k == l:
            continue
        p, q = coord[k][0] - coord[l][0], coord[k][1] - coord[l][1]
        tmp = N
        for i in range(N):
            for j in range(N):
                if coord[i][0] - p == coord[j][0] and coord[i][1] - q == coord[j][1]:
                    tmp -= 1
        ans = min(ans, tmp)

print(ans)