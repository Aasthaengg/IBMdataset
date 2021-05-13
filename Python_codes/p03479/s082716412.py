#n=int(input())
x,y=map(int,input().split())
#l=list(map(int,input().split()))
#l=[list(map(int,input().split())) for i in range(n)]

ans=1
v=x
while v*2<=y:
    ans+=1
    v*=2

print(ans)