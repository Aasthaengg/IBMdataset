from collections import deque
import itertools
def bfs(G,visited,sy,sx):
    queue=deque([[sy,sx]])
    visited[sy][sx]=0
    while queue:
        y,x=queue.popleft()
        if (y,x)== (H-1,W-1):
            return visited[y][x]
        for j,k in ([1,0],[0,1],[-1,0],[0,-1]):
            tmp_y,tmp_x = y+j,x+k
            if 0<=tmp_y<=H-1 and 0<=tmp_x<=W-1 and  G[tmp_y][tmp_x]!='#':
                if visited[tmp_y][tmp_x]==-1:
                    visited[tmp_y][tmp_x]=visited[y][x]+1
                    queue.append([tmp_y,tmp_x])
    return -1
if __name__  =="__main__":
    H,W =map(int,input().split())
    G=[list(input()) for _ in range(H)]
    sy,sx =0,0
    dist=0
    visited=[[-1]*W for _ in range(H)]
    dist=bfs(G,visited,sy,sx)
    if dist==-1:
        print(-1)
    else:
        print(list(itertools.chain.from_iterable(G)).count('.')-dist-1)
