from collections import deque
def start_search(G):
    start=[]
    for i in range(H):
        for j in range(W):
            if G[i][j]=='#':
                start.append((i,j))
    return start
def bfs(G,visited,start):
    queue=deque(start)
    cnt=0
    for p,q in start:
        visited[p][q]=0
    while queue:
        tmp=len(queue)
        for _ in range(tmp):
            (y,x)=queue.popleft()
            for j,k in ([1,0],[0,1],[-1,0],[0,-1]):
                tmp_y,tmp_x = y+j,x+k
                if 0<=tmp_y<=H-1 and 0<=tmp_x<=W-1 and visited[tmp_y][tmp_x]==-1:
                    visited[tmp_y][tmp_x]=visited[y][x]+1
                    queue.append([tmp_y,tmp_x])
        cnt+=1
    return cnt-1
if __name__=="__main__":
    H,W = map(int,input().split())
    G=[input() for _ in range(H)]
    start=start_search(G)
    visited=[[-1]*W for _ in range(H)]
    print(bfs(G,visited,start))
