H,W = map(int,input().split())

s = [list(input()) for y in range(H)]

for y in range(H):
    for x in range(W):
        if s[y][x]=="#":
            enable = False
            if x-1>=0 and s[y][x-1]=="#":
                enable=True
            if x+1<W and s[y][x+1]=="#":
                enable=True
            if y-1>=0 and s[y-1][x]=="#":
                enable=True
            if y+1<H and s[y+1][x]=="#":
                enable=True
            if enable==False:
                print("No")
                exit()
print("Yes")
