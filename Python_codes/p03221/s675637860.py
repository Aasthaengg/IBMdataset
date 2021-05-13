n,m=map(int,input().split())
city=[[0,0,0,0] for _ in range(m)]
for i in range(m):
    p,y=map(int,input().split())
    city[i][0]=p
    city[i][1]=y
    city[i][2]=i
city=sorted(city, key=lambda x:(x[0], x[1]))

cnt=1
for j in range(m):
    ans=''
    ans+='{:06}'.format(city[j][0])
    ans+='{:06}'.format(cnt)
    city[j][3]=ans
    if j==m-1:
        continue
    elif city[j][0]==city[j+1][0]:
        cnt+=1
    else:
        cnt=1
city=sorted(city, key=lambda x:(x[2]))
for k in range(m):
    print(city[k][3])