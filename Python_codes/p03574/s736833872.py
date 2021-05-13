H, W = map(int, input().split())
S = [""]*H
for i in range(H):
    S[i] = list(input())

for i in range(H):
    for j in range(W):
        if S[i][j] != "#":
            num = 0
            
            if i > 0:
                if j > 0:
                    if S[i-1][j-1] == "#":
                        num += 1
                if S[i-1][j] == "#":
                    num += 1
                if j < W-1:
                    if S[i-1][j+1] == "#":
                        num += 1
            if j > 0:
                if S[i][j-1] == "#":
                    num += 1
            if j < W-1:
                if S[i][j+1] == "#":
                    num += 1
            if i < H-1 :
                if j > 0:
                    if S[i+1][j-1] == "#":
                        num += 1
                if S[i+1][j] == "#":
                    num += 1
                if j < W-1:
                    if S[i+1][j+1] == "#":
                        num += 1
            
            S[i][j] = str(num)

for i in range(H):
    print("".join(S[i]))