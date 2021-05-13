h, w = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(h)]
for i in range(h):
    a[i] = [aij % 2 for aij in a[i]]

cnt, ans = 0, []
for i, ai in enumerate(a):
    for j in range(w):
        if i % 2 == 1:
            j = w - 1 - j
        if cnt == 1:
            ans.append([bi + 1, bj + 1, i + 1, j + 1])
            cnt = 0
            ai[j] = (ai[j] + 1) % 2
        if ai[j] == 1:
            cnt = 1
        bi, bj = i, j

print(len(ans))
for q in ans:
    print(*q)
