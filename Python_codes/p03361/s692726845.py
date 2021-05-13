h, w = map(int, input().split())
s = [list(input()) for _ in range(h)]
ans = [[0]*w for _ in range(h)]
cnt=0
def dfs(x,y):
    if 0 <= x < h and 0 <= y < w:
        if s[x][y] == "#" and cnt<2 and ans[x][y]==0:
            ans[x][y] = 1 
            

for i in range(h):
    for j in range(w):
        if s[i][j] == '#':
            dfs(i+1, j)
            dfs(i, j+1)
            dfs(i, j-1)
            dfs(i-1, j)
        cnt=0
for i in range(h):
    for j in range(w):
        if s[i][j] == '#':
            if ans[i][j]!=1:
                print("No")
                exit()
print("Yes")
