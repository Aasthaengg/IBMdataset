H, W = map(int, input().split())
S = [0] * H
for i in range(H):
    S[i] = input()

yoko = [[0] * W for i in range(H)]

for i in range(H):
    for j in range(W):
        if yoko[i][j] != 0:
            continue
        elif S[i][j] == "#":
            yoko[i][j] = 0
        else:
            k = 0
            while S[i][j+k] == ".":
                k += 1
                if j+k == W:
                    break
            yoko[i][j:j+k] = [k] * k

tate = [[0] * W for i in range(H)]

for j in range(W):
    for i in range(H):
        if tate[i][j] != 0:
            continue
        elif S[i][j] == "#":
            tate[i][j] = 0
        else:
            k = 0
            while S[i+k][j] == ".":
                k += 1
                if i+k == H:
                    break
            for l in range(k):
                tate[i+l][j] = k

#for i in range(H):
#    print(tate[i])

ans = 0
for i in range(H):
    for j in range(W):
        ans = max(ans, yoko[i][j] + tate[i][j] - 1)

print(ans)