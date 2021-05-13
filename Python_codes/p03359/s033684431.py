#n=int(input())
a,b=map(int,input().split())
#l=list(map(int,input().split()))
#l=[list(map(int,input().split())) for i in range(n)]
ans=a-1
for day in range(1,b+1):
    if a==day :
        ans+=1
print(ans)


