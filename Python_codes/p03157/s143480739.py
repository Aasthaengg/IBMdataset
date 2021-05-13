H,W = map(int,input().split())
S = [[c==".#"[(i+j)%2] for j,c in enumerate(input())] for i in range(H)]#(0,0)が黒のときFalse
V = [[-1]*W for _ in [0]*H]
ans = 0
for si in range(H):
    for sj in range(W):
        if V[si][sj] != -1:continue
        V[si][sj] = 0
        cnt = [0,0]
        cnt[(S[si][sj]+si+sj)%2]+=1
        q = [[si,sj]]
        while q:
            i,j = q.pop()
            for di,dj in ((1,0),(-1,0),(0,1),(0,-1)):
                if (not (0<=i+di<H)) or (not (0<=j+dj<W)):continue
                if V[i+di][j+dj] != -1:continue
                if S[i][j] != S[i+di][j+dj]:continue
                V[i+di][j+dj] = V[i][j]
                q.append([i+di,j+dj])
                cnt[(S[i][j]+i+di+j+dj)%2] += 1
        ans += cnt[0]*cnt[1]
print(ans)