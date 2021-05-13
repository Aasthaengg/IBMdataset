n,m=map(int,input().split())
List=[]
for i in range(m):
    a,b=map(int,input().split())
    List.append([a,b])
    List.append([b,a])
ans=0
for i in range(1,n+1):
    for j in range(len(List)):
        if i==List[j][0]:
            ans+=1
    print(ans)
    ans=0