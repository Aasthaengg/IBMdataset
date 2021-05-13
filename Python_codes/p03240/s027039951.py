n=int(input())
z=[]
aa=[]
for i in range(n):
     z.append(list(map(int,input().split())))
for cx in range(101):
    for cy in range(101):
        ans=set()
        for i in range(n):
            x,y,h=z[i][0],z[i][1],z[i][2]
            if h!=0:
                tmp=h+abs(x-cx)+abs(y-cy)
                ans.add(tmp)
        if len(ans)==1:
            ans=list(ans)
            aa.append((ans[0],cx,cy))

for a,cx,cy in aa:
    flg=True
    for i in range(n):
        x,y,h=z[i][0],z[i][1],z[i][2]
        if h!=max(a-abs(x-cx)-abs(y-cy),0):
                flg=False
    if flg:
        print(cx,cy,a)
        exit()