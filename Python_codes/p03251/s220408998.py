#n=int(input())
n,m,x,y=map(int,input().split())
xl=list(map(int,input().split()))
yl=list(map(int,input().split()))
#l=[list(map(int,input().split())) for i in range(n)]

ans="War"

for z in range(x+1,y+1,1):
    if max(xl)<z and min(yl)>=z:
        ans="No War"
        break

print(ans)