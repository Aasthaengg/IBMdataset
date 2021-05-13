h,w,k = map(int,input().split())
A = [list(input()) for _ in range(h)]
ans = 0
for i in range(2**w):
    for j in range(2**h):
        grid = [k[:] for k in A]
        cnt = 0
        for p in range(h):
            if (j >> p) & 1:
                grid[p] = ["r"]*w
        for q in range(w):
            if (i >> q) & 1:
                for b in grid:
                    b[q] = "r"
        for x in grid:
            cnt += x.count("#")
        if cnt == k:
            ans += 1
print(ans)