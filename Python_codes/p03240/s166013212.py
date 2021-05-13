n = int(input())
xyh = [list(map(int,input().split())) for i in range(n)]
c = 0
for x,y,h in xyh:
    if h==0:
        c += 1
    else:ans = [x,y,h]
if c==n-1:
    print(*ans)
    exit()

for i in range(101):
    for j in range(101):
        a = -1
        ok = True
        for x,y,h in xyh:
            if h>0:
                if a==-1:
                    a = h+abs(x-i)+abs(y-j)
                elif h+abs(x-i)+abs(y-j)!=a:
                    ok = False
        if ok:
            print(i,j,a)
            exit()
