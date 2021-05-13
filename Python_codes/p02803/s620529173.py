import math , sys

H,W = list(map( int, input().split() ))
maze = []
for i in range(H):
    maze.append(input())
if H==1:
    print(W-1)
    sys.exit()
if W ==1:
    print(H-1)
    sys.exit()

di = [(-1,0),(1,0),(0,1),(0,-1)]
"""
def sol(s,g):
    h = s[0] ; w = s[1]
    gh, gw = g
    d = [[math.inf for _ in range(W)] for _ in range(H)]
    cand = []
    dis = 0
    while True:
        for each in di:
            dh , dw = each
            if h + dh>=0 and h + dh<H and w + dw>=0 and w + dw<W and maze[h+dh][w+dw]=="." and d[h+dh][w+dw]>dis+1:
                cand.append((h+dh, w+dw))
                d[h+dh][w+dw] = dis +1
        if len(cand)==0:
            break
        h , w =cand.pop(0)
        dis = d[h][w]
    return d[g[0]][g[1]]
"""
ans = 0
for h in range(H):
    for w in range(W):
        if maze[h][w]=="#":
            continue
        d = [[math.inf for _ in range(W)] for _ in range(H)]
        cand = []
        dis = 0
        while True:
            for each in di:
                dh , dw = each
                if h + dh>=0 and h + dh<H and w + dw>=0 and w + dw<W and maze[h+dh][w+dw]=="." and d[h+dh][w+dw]>dis+1:
                    cand.append((h+dh, w+dw))
                    d[h+dh][w+dw] = dis +1
                    ans = max(ans, dis+1)
            #print(h,w,cand, d,dis,ans)
            if len(cand)==0:
                break
            h , w =cand.pop(0)
            dis = d[h][w]

print(ans)