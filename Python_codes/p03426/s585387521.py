h,w,d=map(int,input().split())
basyo=[[]for i in range(h*w)]
hako=[]
a=[0 for i in range(h*w)]
for i in range(h):
    hako.append(list(map(int,input().split())))
for i in range(h):
    for j in range(w):
        basyo[hako[i][j]-1].append([i,j])

for i in range(d):
    a[i]=0
    tmp=0
    while i<h*w-d :
        ni=i+d
        t=abs(basyo[i][0][0]-basyo[ni][0][0])+abs(basyo[i][0][1]-basyo[ni][0][1])
        tmp+=t
        a[ni]=tmp
        i=ni
q=int(input())
for i in range(q):
    x,y=map(int,input().split())
    x,y=x-1,y-1
    print(a[y]-a[x])