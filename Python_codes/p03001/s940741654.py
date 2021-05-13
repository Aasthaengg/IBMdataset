W,H,x,y=map(int,input().split())

if x*2==W and y*2==H:
    print(H*W/2,end=" ")
    print(1)
else:
    print(H*W/2,end=" ")
    print(0)