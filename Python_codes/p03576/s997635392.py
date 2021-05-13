n,k=map(int,input().split())
point=[]
for i in range(n):
    x,y=map(int,input().split())
    point.append((x,y))
point.sort()
ans=10**20
for i in range(n):
    for j in range(i+1,n):
        y_list=[]
        for p in range(i,j+1):
            y_list.append(point[p][1])
        y_list.sort()
        yl=len(y_list)
        y_d=10**10
        if yl<k:
            continue
        else:
            for p in range(yl-k+1):
                y_d=min(y_d,y_list[p+k-1]-y_list[p])
        x_d=point[j][0]-point[i][0]
        temp=x_d*y_d
        ans=min(ans,temp)
print(ans)
