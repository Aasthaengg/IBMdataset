H,W = map(int,input().split())
masu = [list(input()) for _ in range(H)]

def koritu(h,w):
    bo=0
    hoko = [[1,0],[0,1],[-1,0],[0,-1]]
    for ya in hoko:
        if 0 <= h+ya[0] < H and 0 <= w+ya[1] < W:
            if masu[h+ya[0]][w+ya[1]] == '#':
                bo = 1
    return bo
   
   
k = 1
for w in range(W):
    for h in range(H):
        if masu[h][w] == '#' and koritu(h,w)==0:
            print('No')
            break
    else:
        continue
    break
else:print('Yes')