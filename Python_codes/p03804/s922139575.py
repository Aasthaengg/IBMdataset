n, m = map(int, input().split())
a = [input() for _ in range(n)]
b = [input() for _ in range(m)]

r = n - m + 1
for i_r in range(r):
    for j_r in range(r):
        ok = True
        for i in range(m):
            for j in range(m):
                if a[i_r + i][j_r + j] != b[i][j]:
                    ok = False
        if ok:
            print('Yes')
            exit(0)

print('No')
