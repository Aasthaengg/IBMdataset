import sys
input = sys.stdin.readline

N = int(input())
xyh = [tuple(map(int, input().split())) for _ in range(N)]
xyh.sort(key=lambda t: t[2], reverse=True)

for cx in range(101):
    for cy in range(101):
        x0, y0, h0 = xyh[0]
        H = h0+abs(x0-cx)+abs(y0-cy)
        flag = True
        
        for x, y, h in xyh:
            h2 = max(H-abs(x-cx)-abs(y-cy), 0)
            
            if h!=h2:
                flag = False
                
        if flag:
            print(cx, cy, H)
            exit()