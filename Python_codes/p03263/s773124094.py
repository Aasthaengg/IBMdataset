H, W = map(int, input().split())
a = [list(map(int, input().split()))for _ in range(H)]
ans = []
for i in range(H):
    for j in range(W-1):
        if a[i][j] % 2 == 1:
            a[i][j] -= 1
            a[i][j+1] += 1
            ans.append([i, j, i, j+1])

w = W - 1
for i in range(H-1):
    if a[i][w] % 2 == 1:
        a[i][w] -= 1
        a[i+1][w] += 1
        ans.append([i, w, i+1, w])
print(len(ans))
aaaa = [list(map(lambda x: x+1, li)) for li in ans]
for x,y,z,a in aaaa:
    print(x, y, z, a)