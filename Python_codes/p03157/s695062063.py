from collections import deque
h,w=map(int,input().split())
p=['-'*(w+2)]
for i in range(h):
    p.append('-'+input()+'-')
p.append('-'*(w+2))

isl=[]
v=[[0 for i in range(w+2)] for j in range(h+2)]
d=[[0,1],[1,0],[-1,0],[0,-1]]

def bfs(x,y):
    if v[x][y]!=0:
        return
    q=deque()
    q.append((x,y))
    v[x][y]=1
    br,wh=0,0
    cnt=0
    while len(q)>0:
        ch,cw=q.popleft()
        #v[ch][cw]=1
        if p[ch][cw]=='#':
            br+=1
            for dh,dw in d:
                if p[ch+dh][cw+dw]=='.' and v[ch+dh][cw+dw]==0:
                    q.append((ch+dh,cw+dw))
                    v[ch+dh][cw+dw]=1
        elif p[ch][cw]=='.':
            wh+=1
            for dh,dw in d:
                if p[ch+dh][cw+dw]=='#' and v[ch+dh][cw+dw]==0:
                    q.append((ch+dh,cw+dw))
                    v[ch+dh][cw+dw]=1
        #print('xy=',x,y,'chw=',ch,cw,'bw=',br,wh,q)
    isl.append((br,wh))

for i in range(1,h+1):
    for j in range(1,w+1):
        bfs(i,j)

ans=0
for br,wh in isl:
    ans+=br*wh

print(ans)