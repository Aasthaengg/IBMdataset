#

import sys
from collections import deque
input=sys.stdin.readline

def main():
    H,W=map(int,input().split())
    masu=[input().strip("\n") for i in range(H)]
    
    di=[(-1,0), (1,0), (0,-1), (0,1)]
    dist=[[-1]*W for i in range(H)]
    ans=0
    
    for i in range(H):
        for j in range(W):
            if masu[i][j]=="#" and dist[i][j]==-1:
                bcnt=0
                wcnt=0
                qu=deque([(i,j)])
                dist[i][j]=0
                while(len(qu)>0):
                    v=qu.popleft()
                    if masu[v[0]][v[1]]=="#":
                        nex="."
                        bcnt+=1
                    else:
                        nex="#"
                        wcnt+=1
                    for d in di:
                        nv=(v[0]+d[0],v[1]+d[1])
                        if 0<=nv[0]<H and 0<=nv[1]<W and dist[nv[0]][nv[1]]==-1 and masu[nv[0]][nv[1]] == nex:
                            dist[nv[0]][nv[1]]=dist[v[0]][v[1]]+1
                            qu.append(nv)
                ans+=bcnt*wcnt
    print(ans)
    
    
if __name__=="__main__":
    main()
