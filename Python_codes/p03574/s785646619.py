h, w = map(int, input().split())
s = [list(input()) for _ in range(h)]
ans = [[0]*w for _ in range(h)]
def dfs(x,y):
    if 0 <= x < h and 0 <= y < w:
        if ans[x][y] != "#":
            ans[x][y] += 1        

for i in range(h):
    for j in range(w):
        if s[i][j] == '#':
            ans[i][j] = '#'
            dfs(i+1, j)
            dfs(i+1, j+1)
            dfs(i+1, j-1)
            dfs(i-1, j+1)
            dfs(i-1, j)
            dfs(i-1, j-1)
            dfs(i, j+1)
            dfs(i, j-1)
for i in range(h):
    for j in range(w):
        ans[i][j]=str(ans[i][j])
        print(ans[i][j],end="")
    print('')

