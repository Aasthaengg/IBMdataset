H,W = map(int,input().split())
S = [list(input()) for _ in range(H)]
#print(S)
ans = [[0]*W for _ in range(H)]
for i in range(H):
    for j in range(W):
        if S[i][j] == "#":
            ans[i][j] = "#"
        else:
            c = 0
            for dx in [-1,0,1]:
                for dy in [-1,0,1]:
                    if 0 <= i+dy <= H-1 and 0 <= j+dx <= W-1 and S[i+dy][j+dx] == "#":
                        c += 1
            ans[i][j] = str(c) 
for i in range(H):
    output = "".join(ans[i])
    print(output)