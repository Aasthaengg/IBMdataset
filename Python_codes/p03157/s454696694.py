import sys
#input = sys.stdin.buffer.readline
from collections import deque

def main():
    H,W = map(int,input().split())
    s = [list(map(str,input())) for _ in range(H)]
    
    dist =[[] for _ in range(H*W)]
    for i in range(H*W):
        x,y = i//W,i%W
        dx,dy = [1,0,-1,0],[0,1,0,-1]
        for j in range(4):
            nx,ny = x+dx[j],y+dy[j]
            if (0<=nx<H and 0<=ny<W and s[x][y]!=s[nx][ny]):
                dist[x*W+y].append(nx*W+ny)

    ans = 0
    go = [False for _ in range(H*W)]
    for i in range(H*W):
        if go[i]:
            continue
        else:
            cc = [0,0]
            queue = deque([i])
            while queue:
                go[i] = True
                now = queue.pop()
                x,y = now//W,now%W
                if s[x][y] == "#":
                    cc[0] += 1
                else:
                    cc[1] += 1
                for fol in dist[now]:
                    if go[fol]:
                        continue
                    else:
                        queue.append(fol)
                        go[fol] = True
        ans += cc[0]*cc[1]
                        
    print(ans)

if __name__ == "__main__":
    main()