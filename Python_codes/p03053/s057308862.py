from collections import deque
H,W=map(int, input().split())
 
A=[]
que=[]
done=[[-1]*W for _ in range(H)]
for h in range(H):
    a=list(input())
    A.append(a)
    for w in range(W):
        if a[w]=="#":
            que.append((h,w))
            done[h][w]=0
 
d=[(1,0),(-1,0),(0,1),(0,-1)]
que=deque(que)
ans=0
while que:
    h,w=que.popleft()
    now=done[h][w]
    for t in d:
        dh,dw=t
        nh=h+dh
        nw=w+dw
        if 0<=nh<H and 0<=nw<W:
            if done[nh][nw]==-1:
                done[nh][nw]=now+1
                que.append((nh,nw))
                ans=max(ans, now+1)
print(ans)
