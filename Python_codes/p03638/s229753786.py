H,W=list(map(int,input().split()))
N=int(input())
a=list(map(int,input().split()))

c=[['']*W for _ in range(H)]
visit=[[0]*W for _ in range(H)]

q=[[0,0,1]]

while len(q)>0:
    h,w,clr=q.pop()
    visit[h][w]=1
    c[h][w]=str(clr)
    a[clr-1]-=1
    if a[clr-1]==0:
        clr+=1

    if h+1<H and visit[h+1][w]==0:
        q.append([h+1,w,clr])
    elif 0<h and visit[h-1][w]==0:
        q.append([h-1,w,clr])
    elif w+1<W and visit[h][w+1]==0:
        q.append([h,w+1,clr])
    
for i in range(H):
    print(' '.join(c[i]))