H, W = map(int,input().split())
c = [["#"]*(W+2) for _ in range(H+2)]
dots = 0
for y in range(H):
    c[y+1] = "#",*list(input()),"#" 
    dots += c[y+1].count(".")
inf = H*W
m = [[inf]*W for _ in range(H)]
m[0][0] = 0
drs = [[-1,0],[1,0],[0,-1],[0,1]]

s = 0
yx = [[1, 1]]
notgoal = True
while notgoal and yx:
    yx2 = []
    s += 1
    for y,x in yx:
        for dy, dx in drs:
            x2 = x+dx
            y2 = y+dy
            if c[y2][x2] == "." and m[y2-1][x2-1] == inf:
                m[y2-1][x2-1] = s
                if (y2,x2) == (H,W):
                    notgoal = False
                else:
                    yx2.append([y2, x2])
    yx = yx2

if notgoal:
    print("-1")
else:
    print(dots-s-1)