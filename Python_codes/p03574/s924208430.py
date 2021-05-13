H, W = map(int,input().split())

S = []
for i in range(H):
    S.append(input())

ans = [[" " for i in range(W)] for j in range(H)]

for i in range(H):
    for j in range(W):
        if S[i][j] == "#":
            ans[i][j] = "#"

        else:
            a = 0
            if i > 0:
                if S[i-1][j] == "#":
                    a += 1
                    
                if j > 0:
                    if S[i-1][j-1] == "#":
                        a += 1

                if j < W-1:
                    if S[i-1][j+1] == "#":
                        a += 1

            if j > 0:
                if S[i][j-1] == "#":
                    a += 1

            if j < W-1:
                if S[i][j+1] == "#":
                    a += 1

            if i < H-1:
                if S[i+1][j] == "#":
                    a += 1
                    
                if j > 0:
                    if S[i+1][j-1] == "#":
                        a += 1

                if j < W-1:
                    if S[i+1][j+1] == "#":
                        a += 1

            ans[i][j] = str(a)

for i in range(H):
  print("".join(ans[i]))