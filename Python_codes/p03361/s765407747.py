#14 C - Grid Repainting 2
H,W = map(int,input().split())
s = [list(input()) for _ in range(H)]

dw = [0,1,0,-1]
dh = [1,0,-1,0]

#ある座標について
result = 'Yes'
for h in range(H):
    for w in range(W):
        #ある座標の上下左右について
        if s[h][w] == '#':
            cnt = 0   
            for i in range(4):
                nxt_w = w + dw[i]
                nxt_h = h + dh[i]
                if not(-1<nxt_w<W) or not(-1<nxt_h<H):
                    continue
                if s[nxt_h][nxt_w] == '#':
                    cnt += 1
            if cnt == 0:
                result = 'No'
                break            
    else:
        continue
    break

print(result)