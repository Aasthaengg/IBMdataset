n=int(input())
if n==1:
    print(1)
    exit()
x=[]
for i in range(n):
    a,b=map(int,input().split())
    x.append([a,b])
x.sort()
ans=float("inf")
for i in range(n-1):
    for j in range(i+1,n):
        p,q=x[j][0]-x[i][0],x[j][1]-x[i][1]
        cnt=0
        flg=[False for i in range(n)]
        for k in range(n):
            if flg[k]==False:
                flg[k]=True
                cnt+=1
                fl=True
                xx,yy=x[k][0],x[k][1]
                while fl:
                    nx,ny=xx+p,yy+q
                    if [nx,ny] in x:
                        a=x.index([nx,ny])
                        flg[a]=True
                        xx,yy=nx,ny
                    else:
                        fl=False
        if cnt<ans:
            ans=cnt
print(ans)