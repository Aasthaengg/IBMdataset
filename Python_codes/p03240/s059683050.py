import sys
input = sys.stdin.readline

N=int(input())
xyh = sorted([ list(map(int,input().split())) for _ in range(N)],key = lambda x:-x[2])

if N==1:
    print(xyh[0],xyh[1],xyh[2])
else:
    for cx in range(101):
        for cy in range(101):
            flag = 0
            dx = abs(cx - xyh[0][0])
            dy = abs(cy - xyh[0][1])
            hmax = xyh[0][2]+dx+dy
            for i in range(1,N):
                if max(hmax -( abs(cx - xyh[i][0])+abs(cy - xyh[i][1])),0) !=  xyh[i][2]:
                    flag = 1
                    break
            if flag == 0:
                print(cx,cy,hmax)
                exit()

        
