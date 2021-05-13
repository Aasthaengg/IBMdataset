n,m=map(int,input().split())
List=[]
for i in range(m):
    road=list(map(int,input().split()))
    List.append(road)
    road=[road[1],road[0]]
    List.append(road)
ans=0
for i in range(1,n+1):
    for j in range(len(List)):
        if i==List[j][0]:
            ans+=1
    print(ans)
    ans=0
