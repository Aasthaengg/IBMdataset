H,W=map(int, input().split())
M=[list(input()) for _ in range(H)]

used=[[False for _ in range(W)] for __ in range(H)]
def dfs(sx,sy):
    global used
    if used[sy][sx]: return (0,0)
    black=white=0
    stack=[(sx,sy)]
    used[sy][sx]=True
    while stack:
        x,y=stack.pop()
        if M[y][x]=='#':
            black+=1
        else:
            white+=1
        for dx,dy in [(1,0),(-1,0),(0,1),(0,-1)]:
            nx,ny=x+dx,y+dy
            if 0<=nx<W and 0<=ny<H and not used[ny][nx]:
                if M[y][x]!=M[ny][nx]:
                    stack.append((nx,ny))
                    used[ny][nx]=True
    return (black,white)

ans=0
for y in range(H):
    for x in range(W):
        black,white=dfs(x,y)
        ans+=black*white
print(ans)
