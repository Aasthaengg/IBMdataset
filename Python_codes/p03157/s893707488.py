from collections import deque
H,W=map(int, input().split())

S=[]
for i in range(H):
    s=list(input())
    S.append(s)



dones=[[0]*W for _ in range(H)]
dh=[1,0,-1,0]
dw=[0,1,0,-1]

def judge(h,w):
    if 0<=h<H and 0<=w<W:
        if dones[h][w]==0:
            return True
    return False
ans=0
for h in range(H):
    for w in range(W):
        now=S[h][w]
        if now=="#" and dones[h][w]==0:
            que=deque([])
            que.append((h, w, "#"))
            dones[h][w]=1
            blacks=0
            whites=0
            while que:
                nowh, noww, color = que.popleft()
                if color=="#":
                    blacks+=1
                    #print(nowh, noww)
                else:
                    whites+=1
                for i in range(4):
                    nh=nowh+dh[i]
                    nw=noww+dw[i]
                    if judge(nh, nw):
                        if color=="#" and S[nh][nw]==".":
                            que.append((nh,nw,"."))
                            dones[nh][nw]=1
                        if color=="." and S[nh][nw]=="#":
                            dones[nh][nw]=1
                            que.append((nh,nw,"#"))
            ans+=blacks*whites
            #print(blacks, whites)

print(ans)