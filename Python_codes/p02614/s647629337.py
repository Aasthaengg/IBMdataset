h,w,k = map(int, input().split())

field = [input() for _ in range(h)]

ans = 0
for i in range(1 << h):
    for j in range(1 << w):
        tmp = 0
        for i1 in range(h):
            for j1 in range(w):
                if (i >> i1) & 1: continue
                if (j >> j1) & 1: continue
                if field[i1][j1] != '#': continue
                tmp += 1
        if tmp == k:
            ans += 1

print(ans)