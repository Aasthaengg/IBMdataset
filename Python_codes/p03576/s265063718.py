n,k=map(int,input().split())
xy=[list(map(int,input().split())) for _ in range(n)]

x_index=set([])
y_index=set([])

for (x,y) in xy:
    x_index.add(x)
    y_index.add(y)
    
####座標圧縮

x_index=list(x_index)
y_index=list(y_index)

x_index.sort()
y_index.sort()
ans=0
for xl in range(len(x_index)-1):
    for xr in range(xl+1,len(x_index)):
        for yl in range(len(y_index)-1):
            for yr in range(yl+1,len(y_index)):
                cnt=0
                for (x,y) in xy:
                    if x_index[xl]<=x and x<=x_index[xr] and y_index[yl]<=y and y<=y_index[yr]:
                        cnt+=1
                if cnt==k:
                    tmp=(x_index[xr]-x_index[xl])*(y_index[yr]-y_index[yl])
                    if ans==0:
                        ans=tmp
                    else:
                        ans=min(ans,tmp)
print(ans)






    
