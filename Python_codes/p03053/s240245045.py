h,w=map(int,input().split())
a=[[] for _ in range(h)]
for i in range(h):
    s=input()
    for j in s:
        if j=='.':
            a[i].append(-1)
        else:
            a[i].append(0)

def bfs():
    d=[[0,1],[1,0],[-1,0],[0,-1]]
    q=[]
    c=-1
    for i in range(h):
        for j in range(w):
            if a[i][j]==0:
                q.append((i,j))
    while q:
        t=q[:]
        q=[]
        c+=1
        for i,j in t:
            for dd in d:
                di,dj=dd[0],dd[1]
                if (i+di)*(h-1-i-di)>=0 and (j+dj)*(w-1-j-dj)>=0 and a[i+di][j+dj]<0:
                    a[i+di][j+dj]=1
                    q.append((i+di,j+dj))
    return(c)

print(bfs())