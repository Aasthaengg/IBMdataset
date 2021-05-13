H,W = map(int,input().split())
S = [list(input()) for i in range(H)]

Rmin = 0
Rmax = 0
Cmin = 0
Cmax = 0

#行方向への探索
for r in range(H):
    #列方向への検索
    for c in range(W):
        #爆弾の場合、周りを加算
        if S[r][c] == ".":
            S[r][c] = 0
        elif S[r][c] == "#":
            if r == 0 and H == 1:
                Rmin = r
                Rmax = 1
            elif r == 0:    
                Rmin = r
                Rmax = r+2
            elif r == H-1:
                Rmin = r-1
                Rmax = r+1
            else:
                Rmin = r-1
                Rmax = r+2

            if c == 0 and W ==1 :
                Cmin = c
                Cmax = 1
            elif c == 0:
                Cmin = c
                Cmax = c+2
            elif c == W-1:
                Cmin = c-1
                Cmax = c+1
            else:
                Cmin = c-1
                Cmax = c+2
            for i in range(Rmin,Rmax):
                for t in range(Cmin,Cmax):
                    if S[i][t] == "." or S[i][t] == 0:
                        S[i][t] = 1
                    elif not S[i][t] == "#":
                        S[i][t] += 1

for i in range(H):
    a = map(str,S[i])
    print(''.join(a))
