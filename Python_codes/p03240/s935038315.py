n = int(input())
xyh = [list(map(int, input().split())) for _ in range(n)]
xyh.sort(key=lambda x: x[2], reverse=True)
#print(xyh)
for cx in range(101):
    for cy in range(101):
        c = (cx, cy)
        count = 0
        H = 0
        for x, y, h in xyh:
            if count == 0:
                H = h+abs(x-cx)+abs(y-cy)
                count = 1
            else:
                if h != max(H-abs(x-cx)-abs(y-cy), 0):
                    break
        else:
            ans = [cx, cy, H]
            print(*ans)
