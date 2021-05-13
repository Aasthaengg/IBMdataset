h,w=map(int,input().split())
grid=[]
for i in range(h):
    *x,=map(int,input().split())
    grid.append(x)
oper=[]
d=[(1,0),(0,1)]
flg=False
cand=[]
for i in range(h):
    if i%2==0:
        s=0
        e=w
        b=1
    else:
        s=w-1
        e=-1
        b=-1
    for j in range(s,e,b):
        if flg:
            grid[i][j]+=1
            flg=False
            cand+=[i+1,j+1]
            oper.append(cand)
            cand=[]
        if grid[i][j]%2==1:
            grid[i][j]-=1
            flg=True
            cand+=[i+1,j+1]

print(len(oper))
for i in oper:
    print(*i)
