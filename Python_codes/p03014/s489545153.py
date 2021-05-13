from sys import stdin
def main():
    #入力
    readline=stdin.readline
    H,W=map(int,readline().split())
    grid=[]
    for i in range(H):
        S=readline().strip()
        grid.append(S)
    up=[[0]*W for _ in range(H)]
    down=[[0]*W for _ in range(H)]
    left=[[0]*W for _ in range(H)]
    right=[[0]*W for _ in range(H)]

    #up,left
    for i in range(H):
        for j in range(W):
            if grid[i][j]==".":
                if i==0:
                    up[i][j]=1
                else:
                    up[i][j]=up[i-1][j]+1
            
                if j==0:
                    left[i][j]=1
                else:
                    left[i][j]=left[i][j-1]+1

    #down,right
    for i in range(H-1,-1,-1):
        for j in range(W-1,-1,-1):
            if grid[i][j]==".":
                if i==H-1:
                    down[i][j]=1
                else:
                    down[i][j]=down[i+1][j]+1

                if j==W-1:
                    right[i][j]=1
                else:
                    right[i][j]=right[i][j+1]+1

    res=0
    for i in range(H):
        for j in range(W):
            if grid[i][j]==".":
                res=max(res,up[i][j]+down[i][j]+left[i][j]+right[i][j]-3)
    
    print(res)
if __name__=="__main__":
    main()