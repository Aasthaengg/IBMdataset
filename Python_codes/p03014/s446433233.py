import sys
input = sys.stdin.readline

H,W = (int(x) for x in input().split())
S = [list(input()) for _ in range(H)]
memh = [[0] * W for _ in range(H)]
memv = [[0] * W for _ in range(H)]
ans = 0
for i in range(H):
    for j in range(W):
        if S[i][j] == '.':
            h = memh[i][j]
            if h == 0:
                stopped = False
                for k in range(W-j-1):
                    if S[i][j+k+1] == '#':
                        for l in range(k+1):
                            memh[i][j+l] = k+1
                        stopped = True
                        break
                if stopped == False:
                    for l in range(W-j):
                        memh[i][j+l] = W-j
                h = memh[i][j]
            v = memv[i][j]
            if v == 0:
                stopped = False
                for k in range(H-i-1):
                    if S[i+k+1][j] == '#':
                        for l in range(k+1):
                            memv[i+l][j] = k+1
                        stopped = True
                        break
                if stopped == False:
                    for l in range(H-i):
                        memv[i+l][j] = H-i
                v = memv[i][j]
            ans = max(ans,h+v-1)
print(ans)