import math
A,B = map(int,input().split())
x1 = math.ceil(A / 0.08)
x2 = (A+1) / 0.08
y1 = math.ceil(B / 0.10)
y2 = (B+1) / 0.10

while x1 < x2:
    if y1 <= x1 < y2:
        print(x1)
        exit(0)
    x1 += 1
print(-1)