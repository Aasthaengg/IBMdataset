H, W = map(int, input().split())
S = [list(input()) for _ in range(H)]

#   .
# . # .
#   .
# を探す

for i in range(H):
    for j in range(W):
        if S[i][j] == "#":
            temp = set()
            if i != 0:
                temp.add(S[i-1][j])
            if i != H-1:
                temp.add(S[i+1][j])
            if j != 0:
                temp.add(S[i][j-1])
            if j != W-1:
                temp.add(S[i][j+1])
            if temp == set("."):
                print("No")
                exit()

print("Yes")