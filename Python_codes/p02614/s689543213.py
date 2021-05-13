h, w, k = map(int, input().split())
c = [list(input()) for i in range(h)]
ans = 0
for p in range(1<<h):
    for q in range(1<<w):
        black = 0
        for m in range(h):
            for n in range(w):
                if (p>>m)&1 == 0 and (q>>n)&1 == 0 and c[m][n] == "#":
                    black += 1
        if black == k:
            ans += 1
print(ans)