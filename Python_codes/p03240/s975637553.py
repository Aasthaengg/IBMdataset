#c
N=int(input())
XYH = [None]*N
for i in range(N):
    XYH[i] = list(map(int,input().split()))

for cx in range(101):
    for cy in range(101):
        found=False
        for i in range(N):
            d = abs(XYH[i][0]-cx)+abs(XYH[i][1]-cy)
            if XYH[i][2]>0 and not found:
                h = XYH[i][2]+d
                break
        for i in range(N):
            d = abs(XYH[i][0]-cx)+abs(XYH[i][1]-cy)
            if XYH[i][2]!= max(0,h-d):
                break
        else:
            print(cx,cy,h)