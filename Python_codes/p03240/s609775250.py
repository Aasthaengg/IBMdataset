n = int(input())
xyh = []
for _ in range(n):
    x, y, h = map(int, input().split())
    xyh.append((x, y, h))
for cx in range(101):
    for cy in range(101):
        H = None
        maxH = 10**12
        for x, y, h in xyh:
            if h>0:
                if H is None:
                    H = h+abs(x-cx)+abs(y-cy)
                elif H!=h+abs(x-cx)+abs(y-cy):
                    break
                if H>maxH:
                    break
            else:
                maxH = min(maxH, abs(x-cx)+abs(y-cy))
                if H is not None and H>maxH:
                    break
        else:
            print(cx, cy, H)
            exit()