N=int(input())
t,x,y=0,0,0
for i in range(N):
    T,X,Y=map(int,input().split())
    r=abs(X-x)+abs(Y-y)
    t=T-t
    if r%2!=t%2 or t<r:
        print('No')
        exit()
    t=T;x=X;y=Y
print('Yes')