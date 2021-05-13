n,A,B,C=map(int,input().split())
l=[]
for _ in range(n):
    l.append(int(input()))
def solve(cur,a,b,c):
    if cur==n:
        #base case
        return abs(a-A)+abs(b-B)+abs(c-C)-30 if min(a,b,c)>0 else float('INF')
    ret0=solve(cur+1,a,b,c)
    ret1=solve(cur+1,a+l[cur],b,c)+10
    ret2=solve(cur+1,a,b+l[cur],c)+10
    ret3=solve(cur+1,a,b,c+l[cur])+10
    return min(ret0,ret1,ret2,ret3)
print(solve(0,0,0,0))
