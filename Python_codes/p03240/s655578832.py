N = int(input())
xyh = [list(map(int, input().split())) for i in range(N)]
# print(N, xyh)

height = None
found = False
for cx in range(0, 101):
    for cy in range(0, 101):
        candidate = 0
        for x, y, h in xyh:
            if h == 0: continue
            dx = abs(x - cx)
            dy = abs(y - cy)
            candidate = dx + dy + h 
            break

        found = True
        for x, y, h in xyh:
            _h = max(candidate - abs(x - cx) - abs(y - cy), 0)
            if h != _h:
                found = False
                break
        
        if found is True: break
    if found is True: break
height = candidate if candidate is not None else 0

print(cx, cy, height)
