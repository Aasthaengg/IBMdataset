from collections import deque

H,W=map(int,input().split())
S=[]
for i in range(H):
    S.append(input())

q=deque([])
T=[]
seen=[[0]*W for _ in range(H)]
step=[[0,1],[0,-1],[1,0],[-1,0]]
for h in range(H):
    for w in range(W):
        temp=[]
        if seen[h][w]==0:
            temp.append(S[h][w])
            seen[h][w]=1
            q.append([h,w,S[h][w]])
            while q:
                oh,ow,m=q.popleft()
                for dh,dw in step:
                    if 0<=oh+dh<H and 0<=ow+dw<W:
                        if seen[oh+dh][ow+dw]==0 and m!=S[oh+dh][ow+dw]:
                            temp.append(S[oh+dh][ow+dw])
                            seen[oh+dh][ow+dw]=1
                            q.append([oh+dh,ow+dw,S[oh+dh][ow+dw]])
            T.append(temp)

ans=0
for i in range(len(T)):
    black=0
    white=0
    for s in T[i]:
        if s=="#":
            black+=1
        else:
            white+=1
    ans+=black*white

print(ans)


