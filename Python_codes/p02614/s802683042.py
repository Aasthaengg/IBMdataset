h, w, k = map(int, input().split())
c = [list(input()) for _ in range(h)]

ans = 0
for i in range(2**h):
    for j in range(2**w):
        cnt = 0
        for ii in range(h):
            for jj in range(w):
                if (i>>ii)&1 == 1 and (j>>jj)&1 == 1:
                    if c[ii][jj] == '#':
                        cnt += 1
        if cnt == k:
            ans += 1
print(ans)
