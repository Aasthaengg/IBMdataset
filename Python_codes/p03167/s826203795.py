def main():
    import sys
    input=sys.stdin.readline
    from collections import deque
    H,W=map(int,input().split())
    maze=[]
    for _ in range(H):
        a=input().rstrip()
        maze.append(a)
    path=[[0]*W for _ in range(H)]
    path[0][0]=1
    q=deque([[0,0]])
    finished=[[False]*W for _ in range(H)]
    while q:
        h,w=q.popleft()
        if finished[h][w]==True:
            continue
        for nh,nw in ([h+1,w],[h,w+1]):
            if nh<0 or nh>H-1 or nw<0 or nw>W-1:
                continue
            if maze[nh][nw]=="#":
                continue
            path[nh][nw]+=path[h][w]
            path[nh][nw]%=1000000007
            q.append([nh,nw])
        finished[h][w]=True
    print(path[-1][-1])

if __name__=="__main__":
    main()