H, W = map(int, input().split())
S = [""]*H
for i in range(H):
    S[i] = list(input())

for i in range(H):
    for j in range(W):
        if S[i][j] == "#":
            
            if i > 0:
                if S[i-1][j] == "#":
                    continue
            if j > 0:
                if S[i][j-1] == "#":
                    continue
            if j < W-1:
                if S[i][j+1] == "#":
                    continue
            if i < H-1 :
                if S[i+1][j] == "#":
                    continue
                
            print("No")
            exit()

print("Yes")