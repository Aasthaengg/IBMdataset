import collections
n=int(input())
xy=[list(map(int,input().split())) for _ in range(n)]
xy.sort()
count={}
ans=0
for i in range(n):
    for j in range(i+1,n):
   #     print(i,j)
        x=xy[i][0]-xy[j][0]
        y=xy[i][1]-xy[j][1]
        if (x,y) in count:
            count[x,y]+=1
        else:
            count[x,y]=1
#print(count)
for v in count.values():
    ans=max(ans,v)
print(n-ans)