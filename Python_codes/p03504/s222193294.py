n, cc = [int(i) for i in input().split()]
up = [[0] * (2 * 10 ** 5) for _ in range(cc)]
ch = [[0] * (2 * 10 ** 5) for _ in range(cc)]

for _ in range(n):
    s, t, c = map(int, input().split())
    c -= 1
    up[c][s] += 1
    up[c][t] -= 1

for j in range(cc):
    k = 0
    for i in range(2 * 10 ** 5):
        if up[j][i] == 1:
            k = 1
        ch[j][i] = k
        if up[j][i] == -1:
            k = 0
ans = 0
for i in range(2 * 10 ** 5):
    k = 0
    for j in range(cc):
        k += ch[j][i]
    ans = max(ans, k)
print(ans)
