import sys
input = sys.stdin.readline

H,W=map(int,input().split())
S = []
for _ in range(H):
    S.append(list(input().strip()))

for i in range(H):
    for j in range(W):
        if S[i][j] == '#':
            continue
        c = 0
        for ii in range(i-1,i+2):
            if ii < 0 or ii >= H:
                continue
            for jj in range(j-1,j+2):
                if jj < 0 or jj >= W:
                    continue
                if S[ii][jj] == '#':
                    c += 1
        S[i][j] = str(c)

for row in S:
    print("".join(row))
