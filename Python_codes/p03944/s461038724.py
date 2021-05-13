W, H, N = map(int, input().split())
minX = 0
maxX = W
minY = 0
maxY = H
for i in range(N):
    x, y, a = map(int, input().split())
    if a == 1:
        minX = max(minX, x)
    elif a == 2:
        maxX =min(maxX, x)
    elif a == 3:
        minY = max(minY, y)
    elif a == 4:
        maxY = min(maxY, y)

print(max(0, maxX-minX)*max(0, maxY-minY))