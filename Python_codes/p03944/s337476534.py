W,H,N = map(int,input().split())

x_m,x_M,y_m,y_M = 0, W, 0, H

for i in range(N):
    x,y,A = map(int,input().split())
    if A == 1:
        x_m = max(x, x_m)
    if A == 2:
        x_M = min(x, x_M)
    if A == 3:
        y_m = max(y, y_m)
    if A == 4:
        y_M = min(y, y_M)

print(max(0, x_M - x_m) * max(0, y_M - y_m))