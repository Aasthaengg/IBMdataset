import sys,math,collections,itertools
input = sys.stdin.readline

H,W=list(map(int,input().split()))
s = [input().rstrip() for _ in range(H)]
memo = [[0]*W for _ in range(H)]
memo[0][0]=1
q = collections.deque([[0,0]])
while q:
    h,w = q.popleft()
    if h>0 and s[h-1][w]=='.' and memo[h-1][w]==0:
        q.append([h-1,w])
        memo[h-1][w] = memo[h][w] +1
    if h<H-1 and s[h+1][w]=='.' and memo[h+1][w]==0:
        q.append([h+1,w])
        memo[h+1][w] = memo[h][w] +1
    if w>0 and s[h][w-1]=='.' and memo[h][w-1]==0:
        q.append([h,w-1])
        memo[h][w-1] = memo[h][w] +1
    if w<W-1 and s[h][w+1]=='.' and memo[h][w+1]==0:
        q.append([h,w+1])
        memo[h][w+1] = memo[h][w] +1
if memo[H-1][W-1] == 0:
    print(-1)
else:
    cnt = 0
    for i in range(H):
        cnt += s[i].count('#')
    print(H*W-cnt-memo[H-1][W-1])
