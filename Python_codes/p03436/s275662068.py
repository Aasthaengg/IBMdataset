from collections import deque
H,W=map(int,input().split())
maze=[list(input()) for i in range(H)]
count=-1

#-------------------------------------------------------------------------
#幅優先探索,再帰関数

def search() :
    flag=[[0]*W for i in range(H)]
    count=[[-1]*W for i in range(H)]
    flag[0][0]=1                               #通った場所はflagを0から1に変更していく
    count[0][0]=0                              #こちらで通る時間を数える
    pos=deque([])
    pos.append([0,0])

    while len(pos)>0 :
        y,x=pos.popleft()
        if y==H-1 and x==W-1 :
            return count[H-1][W-1]
            break

        for p,q in [[1,0],[-1,0],[0,1],[0,-1]] :
            if 0<=y+p<H and 0<=x+q<W and maze[y+p][x+q]=="." and flag[y+p][x+q]==0 :
                flag[y+p][x+q]=1     
                pos.append([y+p,x+q])
                count[y+p][x+q]=count[y][x]+1    

    if y!=H-1 and x!=W-1 :
        print(-1)
        exit()         

#-------------------------------------------------------------------------
#スコア求める,始めに白の個数を数えて、後で通った白の数だけ引く

for i in range(H) :
    for j in range(W) :
        if maze[i][j]=="." :    
            count+=1

ans=count-search()

print(ans)
