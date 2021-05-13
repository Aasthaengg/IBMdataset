H, W = map(int, input().split())
S = [["."] + list(input()) + ["."] for _ in range(H)]
S = [["."]*(W+2)] + S + [["."]*(W+2)]

ans = "Yes"
for i in range(1,H+1):
    for j in range(1,W+1):
        if S[i][j] == "#":
            UDLR = [S[i-1][j], S[i+1][j], S[i][j-1], S[i][j+1]]
            if "#" in UDLR:
                pass
            else:
                ans = "No"
                break

print(ans)
