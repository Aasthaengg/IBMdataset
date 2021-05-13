h , w = map(int,input().split())
giri = [list(input()) for i in range(h)]
ans = [[0 for i in range(w)] for j in range(h)]
for i in range(h):
    sta = -1
    cou = 0
    for j in range(w):
        if sta == -1 and giri[i][j] == ".":
            sta = j
            cou += 1
        elif sta != -1 and giri[i][j] == ".":
            cou += 1
        elif sta != -1 and giri[i][j] == "#":
            for k in range(sta,j):
                ans[i][k] += cou
            cou = 0
            sta = -1
        if j == w-1 and sta != -1:
            for k in range(sta,w):
                ans[i][k] += cou

for i in range(w):
    sta = -1
    cou = 0
    for j in range(h):
        if sta == -1 and giri[j][i] == ".":
            sta = j
            cou += 1
        elif sta != -1 and giri[j][i] == ".":
            cou += 1
        elif sta != -1 and giri[j][i] == "#":
            for k in range(sta,j):
                ans[k][i] += cou
            cou = 0
            sta = -1
        if j == h-1 and sta != -1:
            for k in range(sta,h):
                ans[k][i] += cou

kotae = 0

for i in range(h):
    for j in range(w):
        kotae = max(kotae,ans[i][j]-1)

print(kotae)