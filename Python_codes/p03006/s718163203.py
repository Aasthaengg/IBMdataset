from bisect import bisect_left
N=int(input())
xy=[list(map(int,input().split())) for i in range(N)]
xy.sort()
inf=float("inf")
ans=inf
for i in range(N-1):
    for j in range(i+1,N):
        p=xy[j][0]-xy[i][0]
        q=xy[j][1]-xy[i][1]
        flag=[0]*N
        cnt=0
        for k in range(N):
            if flag[k]==0:
                flag[k]=1
                cnt+=1
                nx,ny=xy[k][0]+p,xy[k][1]+q
                b=bisect_left(xy,[nx,ny])
                while b<N and xy[b]==[nx,ny]:
                    flag[b]=1
                    nx,ny=nx+p,ny+q
                    b=bisect_left(xy,[nx,ny])
        ans=min(ans,cnt)
if N==1:
    print(1)
else:
    print(ans)