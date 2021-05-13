h, w, k = map(int, input().split())
s = [input() for _ in range(h)]

INF = 10 ** 20
ans = INF
for div in range(1 << (h - 1)):
    id = []
    g = 0
    for i in range(h):
        id.append(g)
        if div >> i & 1:
            g += 1
    g += 1

    c = [[0 for _ in range(w)] for _ in range(g)]
    for i in range(h):
    	for j in range(w):
            c[id[i]][j] += (s[i][j] == "1")

    if max([max(l) for l in c]) > k:
        continue

    tmp_ans = g - 1
    now = [0] * g

    for j in range(w):
        for i in range(g):
            now[i] += c[i][j]
            if now[i] > k:
                tmp_ans += 1
                now = [c[gi][j] for gi in range(g)]
                break

    ans = min(ans, tmp_ans)

print(ans)