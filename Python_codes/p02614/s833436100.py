h,w,k = map(int,input().split())
c = [list(input()) for i in range(h)]
ans = 0
for i in range(2**h):
    h_list = [False] * h
    for j in range(h):
        if (i >> j) & 1:
            h_list[h - 1 - j] = True
    
    for l in range(2**w):
        w_list = [False] * w
        for m in range(w):
            if (l >> m) & 1:
                w_list[w - 1 - m] = True

        cnt = 0
        for a in range(h):
            for b in range(w):
                if c[a][b] == '#' and not h_list[a] and not w_list[b]:
                    cnt += 1
        if cnt == k:
            ans += 1
print(ans)