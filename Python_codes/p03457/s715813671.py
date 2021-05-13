N=int(input())
ct,cx,cy=0,0,0
for i in range(N):
    t,x,y=map(int,input().split())
    dt=t-ct
    dx=x-cx
    dy=y-cy
    if dt<abs(dx)+abs(dy):
        print('No')
        exit()
    elif (dt-(abs(dx)+abs(dy)))%2!=0:
        print('No')
        exit()
    ct=t
    cx=x
    cy=y


print('Yes')