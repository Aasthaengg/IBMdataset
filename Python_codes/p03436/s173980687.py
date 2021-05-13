def main():
    h,w=map(int,input().split())
    maze=["#"*(w+2)]+["#"+input()+"#" for _ in range(h)]+["#"*(w+2)]
    total_white=sum([row.count(".") for row in maze])

    seen=[[-1]*(w+2) for _ in range(h+2)]
    if maze[1][1]=="#" : print(-1);exit()
    seen[1][1]=1
    token=1
    bfs_new=[(1,1)]

    while bfs_new:
        token+=1
        bfs_old=bfs_new[:]
        bfs_new=[]
        for x in bfs_old:
            for move in [(1,0),(-1,0),(0,1),(0,-1)]:
                ywork=x[0]+move[0]
                xwork=x[1]+move[1]
                if maze[ywork][xwork]=="#" : continue
                if seen[ywork][xwork]>=0 : continue
                seen[ywork][xwork]=token
                bfs_new.append((ywork,xwork))
    
    if seen[h][w]==-1 : print(-1)
    else : print(total_white-seen[h][w])

main()