import sys
sys.setrecursionlimit(10**8)

H, W = map(int,input().split())
S = [input() for _ in range(H)]
#%%
visited = [[False]*W for _ in range(H)]
dx = [1,0,-1,0]
dy = [0,1,0,-1]

group_w = [0]*(H*W)
group_k = [0]*(H*W)

def dfs(x,y,state):
    if S[x][y]=='.':
        group_w[idx] += 1
    else:
        group_k[idx] += 1
    visited[x][y] = True
    
    for i in range(4):
        nx = x+dx[i]
        ny = y+dy[i]
        if nx<0 or nx>=H or ny<0 or ny>=W:
            continue
        if visited[nx][ny]:
            continue
        if state==0 and S[nx][ny]=='#':
            dfs(nx,ny,1)
        elif state==1 and S[nx][ny]=='.':
            dfs(nx,ny,0)
    return 


ans = 0
idx = 0
for i in range(H):
    for j in range(W):
        if not visited[i][j]:
            dfs(i,j,S[i][j]=='#')
            a = group_w[idx]
            b = group_k[idx]
            ans += a*b
            idx += 1
       
print(ans)






# def dfs(x,y,res, numW,numK,state):
#     # print(x,y,res)
#     # state=0: next=Black
#     # state=1: next=White
#     newres = 0
#     flag = True
#     for i in range(4):
#         nx = x+dx[i]
#         ny = y+dy[i]
#         if nx<0 or nx>=H or ny<0 or ny>=W:
#             continue
#         if visited[nx][ny]:
#             continue
#         if state==0 and S[nx][ny]=='#':
#             visited[nx][ny] = True
#             newres += dfs(nx,ny,res+numW,numW,numK+1,1)
#             flag = False
#         elif state==1 and S[nx][ny]=='.':
#             visited[nx][ny] = True
#             newres += dfs(nx,ny,res+numK,numW+1,numK,0)
#             flag = False
    
#     # if flag:
#     #     visited[x][y] = False
#     if S[x][y]=='.':
#         return newres + numK
#     elif S[x][y]=='#':
#         return newres + numW

# ans = 0
# for i in range(H):
#     for j in range(W):
#         if not visited[i][j]:
#             numW = S[i][j]=='.'
#             numK = S[i][j]=='#'
#             visited[i][j] = True
#             ans += dfs(i,j,0,numW,numK,numK)
#             # print('X,Y =',i,j,ans)

# print(ans)