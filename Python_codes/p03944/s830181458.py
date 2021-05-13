w, h, n = map(int, input().split())
x1 = 0
y1 = 0
x2 = w
y2 = h
f = 0
for i in range(n):
    x, y, a = map(int, input().split())
    if a == 1:
        x1 = max(x, x1)
    elif a == 2:
        x2 = min(x, x2)
    elif a == 3:
        y1 = max(y, y1)
    elif a == 4:
        y2 = min(y, y2)
    
    if x1 >= x2 or y1 >= y2 or x2 <= 0 or y2 <= 0:
        f = 1
if f:
    print("0")
else:
    print((x2-x1)*(y2-y1))