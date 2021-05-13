from collections import defaultdict

def dfs(i,j,dx,dy,kum):
    visited[i][j] = 1
    if grid[i][j]!="#" and visited[i][j]!=1:
        num[i][j]=max(num[i][j],dfs(i+dx,j+dy,dx,dy,kum+1))
    num[i][j] = max(num[i][j],kum)
    return kum
def main():
    h,w = map(int, input().split())
    grid = []
    for i in range(h):
        s = list(input().rstrip())
        grid.append(s)
    l = [[0]*w for _ in range(h)]
    r = [[0]*w for _ in range(h)]
    d = [[0]*w for _ in range(h)]
    u = [[0]*w for _ in range(h)]
    for i in range(h):
        for j in range(w):
            if grid[i][j]!="#":
                if j==0:
                    l[i][j]=1
                else:
                    l[i][j]=l[i][j-1]+1
            if grid[i][j]=="#":
                l[i][j]=0
    for i in range(h):
        for j in range(w-1,-1,-1):
            if grid[i][j]!="#":
                if j==w-1:
                    r[i][j]=1
                else:
                    r[i][j]=r[i][j+1]+1
            if grid[i][j]=="#":
                r[i][j]=0
    for i in range(h):
        for j in range(w):
            if grid[i][j]!="#":
                if i==0:
                    d[i][j]=1
                else:
                    d[i][j]=d[i-1][j]+1
            if grid[i][j]=="#":
                d[i][j]=0
    for i in range(h-1,-1,-1):
        for j in range(w):
            if grid[i][j]!="#":
                if i==h-1:
                    u[i][j]=1
                else:
                    u[i][j]=u[i+1][j]+1
            if grid[i][j]=="#":
                u[i][j]=0
    tmp = 0

    for i in range(h):
        for j in range(w):
            tmp = max(tmp, l[i][j]+r[i][j]+u[i][j]+d[i][j]-3)



    print(tmp)

if __name__ == '__main__':
    main()
