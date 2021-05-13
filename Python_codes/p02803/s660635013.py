#D
import queue
H,W=map(int,input().split())
P=[0 for i in range(H)]
for i in range(H):
    P[i]=str(input())
ans=0
for i in range(H*W):
    s=(i//W,i%W)
    if P[s[0]][s[1]]=="#":
        continue
    st=queue.Queue()
    st.put(s)
    log=[[-1 for i in range(W)] for j in range(H)]
    log[s[0]][s[1]]=0
    while not st.empty():
        y,x=st.get()
        for z,w in [(y+1,x),(y-1,x),(y,x+1),(y,x-1)]:
            if 0>z or 0>w:
                continue
            elif z>=H or w>=W:
                continue
            elif P[z][w]=="." and log[z][w]==-1:
                st.put((z,w))
                log[z][w]=log[y][x]+1
                ans=max(ans,log[z][w])
print(ans)