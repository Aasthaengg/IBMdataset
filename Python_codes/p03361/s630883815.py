H,W = map(int,input().split())
S = [input() for _ in range(H)]
A = [(1,0),(0,1),(-1,0),(0,-1)]
for i in range(H):
    for j in range(W):
        if S[i][j] == "#":
            bol = 0
            for dx,dy in A:
                if 0<=j+dx<=W-1 and 0<=i+dy<=H-1:
                    if S[i+dy][j+dx] == "#":
                        bol = 1
            if bol == 0:
                print("No")
                exit()
print("Yes")