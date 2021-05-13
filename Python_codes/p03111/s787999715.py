N,A,B,C = map(int,input().split())
l = [int(input()) for i in range(N)]
INF = 100000000
def rec(i,a,b,c):
    if(i==N):
        return(abs(a-A)+abs(b-B)+abs(c-C)-30 if min(a,b,c)>0 else INF)
    ret0 = rec(i+1,a,b,c)
    ret1 = rec(i+1,a+l[i],b,c)+10
    ret2 = rec(i+1,a,b+l[i],c)+10
    ret3 = rec(i+1,a,b,c+l[i])+10
    return min(ret0,ret1,ret2,ret3)
print(rec(0,0,0,0))
