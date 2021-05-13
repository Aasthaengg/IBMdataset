from collections import deque
H,W = map(int,input().split())
S = [input() for i in range(H)]
ans = 0
flag = [[0]*W for i in range(H)]
for i in range(H*W):
    x,y = i%W,i//W
    if flag[y][x] == 1:
        continue
    flag[y][x] = 1
    bw = [0,0]
    bw[[".","#"].index(S[y][x])]+=1
    queue = deque([[x,y]])
    while queue:
        x,y = queue.popleft()
        for a,b in [[-1,0],[1,0],[0,1],[0,-1]]:
            if 0<=x+a<W and 0<=y+b<H and flag[y+b][x+a] == 0 and S[y][x] != S[y+b][x+a]:
                queue.append([x+a,y+b])
                flag[y+b][x+a] = 1
                bw[[".","#"].index(S[y+b][x+a])]+=1
    ans += bw[0]*bw[1]
print(ans)
                


             
