n = int(input())
xyh = [tuple(map(int,input().split())) for i in range(n)]
for xi,yi,hi in xyh:
    if hi:
        xt,yt,ht = xi,yi,hi

for i in range(101):
    for j in range(101):
        a = ht+abs(i-xt)+abs(j-yt)
        for xi,yi,hi in xyh:
            x = max(a - abs(xi-i)-abs(yi-j),0)
            if hi != x:
                break
        else:
            print(i,j,a)
            exit(0)
