N, W = map(int, input().split())
w, v = [None] * N, [None] * N
for i in range(N):
    w[i], v[i] = map(int, input().split())
wmin = w[0]
_w = [[], [], [], []]
for i in range(N):
    _w[w[i] - wmin].append(v[i])
for i in range(4):
    _w[i].sort(reverse = 1)
    for j in range(1, len(_w[i])):
        _w[i][j] += _w[i][j-1]
    _w[i].insert(0, 0)
ans = 0
for c0 in range(len(_w[0])):
    for c1 in range(len(_w[1])):
        for c2 in range(len(_w[2])):
            for c3 in range(len(_w[3])):
                if wmin * (c0 + c1 + c2 + c3) + c1 + 2 * c2 + 3 * c3 <= W:
                    ans = max(ans, _w[0][c0] + _w[1][c1] + _w[2][c2] + _w[3][c3])
print(ans)
