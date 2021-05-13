H,W = map(int,input().split())

S = [list(input()) for i in range(H)]

for i in range(H):
    for j in range(W):
        ans = 0
        if S[i][j]=='.':
            for h in range(max(0,i-1),min(H,i+2)):
                for w in range(max(0,j-1),min(W,j+2)):
                    if S[h][w]=='#':
                        ans += 1
            S[i][j] = str(ans)
        
for i in range(H):
    print(''.join(S[i]))