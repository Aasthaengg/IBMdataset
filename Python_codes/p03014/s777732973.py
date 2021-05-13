def main():
    import sys
    input=sys.stdin.readline
    H,W=map(int,input().split())
    maze=[]
    for _ in range(H):
        s=input().rstrip()
        maze.append(s)
    lamp=[[0]*W for _ in range(H)]
    for i in range(H):
        num=0
        for j in range(W):
            if maze[i][j]=="#":
                for k in range(1,num+1):
                    lamp[i][j-k]=num
                num=0
            else:
                num+=1
                if j==W-1:
                    for k in range(num):
                        lamp[i][j-k]=num
    for i in range(W):
        num=0
        for j in range(H):
            if maze[j][i]=="#":
                for k in range(1,num+1):
                    lamp[j-k][i]+=num
                num=0
            else:
                num+=1
                if j==H-1:
                    for k in range(num):
                        lamp[j-k][i]+=num
    lamp=[i for j in lamp for i in j]
    print(max(lamp)-1)
    
if __name__=="__main__":
    main()