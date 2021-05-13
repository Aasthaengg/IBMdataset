H, W, K = list(map(int, input().split()))
c = []
for i in range(H):
    c.append(list(input()))

ans = 0
for i in range(2**H):
    for j in range(2**W):
        count = 0
        for k in range(H):
            for l in range(W):
                if (i>>k) & 1:
                    if (j>>l) & 1:
                        if c[k][l] == "#":
                           count += 1
        if count == K:
            ans += 1

print(ans)
