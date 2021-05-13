H, W = map(int, input().split())
pic = [[i for i in input()] for j in range(H)]
ans = [["#" for i in range(W+2)] for j in range(H+2)]

for h in range(H):
    for w in range(W):
        ans[h+1][w+1] = pic[h][w]
        
for i in range(H+2):
    for j in range(W+2):
        print(ans[i][j], end="")
    print()