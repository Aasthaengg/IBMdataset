H, W = list(map(int,input().split()))
s = []
for i in range(H):
    s.append(input())
r = "Yes"
for i in range(H):
    for j in range(W):
        if s[i][j]==".":
            continue
        p = False
        for y,x in [[i-1,j],[i+1,j],[i,j-1],[i,j+1],]:
            if 0<=y<H and 0<=x<W and s[y][x]=="#":
                p = True
        if not p:
            r = "No"
print(r)