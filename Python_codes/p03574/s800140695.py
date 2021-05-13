H, W = list(map(int,input().split()))
S = []
c = []
for h in range(H):
    S.append(input())
    c.append([0 for _ in range(W)])
for y in range(H):
    for x in range(W):
        if S[y][x]=="#":
            continue
        for cy in range(max(0,y-1),min(H,y+2)):
            for cx in range(max(0,x-1),min(W,x+2)):
                c[y][x] += 1 if ( (cy!=y or cx!=x) and S[cy][cx]=="#" ) else 0
for y in range(H):
    for x in range(W):
        print("#" if S[y][x]=="#" else c[y][x], end="")
    print("")