import sys
input = sys.stdin.readline

W,H,N = list(map(int,input().split()))
x0 = 0
y0 = 0
x1 = W
y1 = H

for i in range(N):
    x,y,a = list(map(int,input().split()))

    if a == 1:
        x0 = max(x,x0)
    elif a == 2:
        x1 = min(x,x1)
    elif a == 3:
        y0 = max(y,y0)
    elif a == 4:
        y1 = min(y,y1)
X = [x0,x1,y0,y1]

print(max(0,x1-x0)*max(0,y1-y0))
