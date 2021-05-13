n, m = map(int, input().split())
xyz = [list(map(int, input().split())) for _ in range(n)]

ans = 0

for i in range(8):
    tmp = [0, 0, 0]
    for j in range(3):
        if i & (1 << j):
            tmp[j] = 1
    S = []
    for item in xyz:
        val = item[:]
        for j in range(3):
            if tmp[j]:
                val[j] *= -1
        S.append(sum(val))
    S.sort(reverse=True)
    ans = max(ans, sum(S[:m]))

print(ans)


