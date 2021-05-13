H,W = map(int, input().split())
s = [list(input()) for _ in range(H)]

bom = []
for i in range(H):
    for j in range(W):
        if s[i][j] == ".": s[i][j] = 0
        else: bom.append([i,j])

for i in range(len(bom)):
    h,w = bom[i][0], bom[i][1]
    for x,y in ([1,0], [-1,0], [0,1], [0,-1], [1,1], [-1,-1], [1,-1], [-1,1]):
        new_h, new_w =  h+x, w+y
        if new_h<0 or new_h>=H or new_w<0 or new_w>=W: continue
        if s[new_h][new_w] != "#":
            s[new_h][new_w] += 1
for ans in s:
    print("".join(list(map(str, ans))))