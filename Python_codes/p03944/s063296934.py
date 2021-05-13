(w, h, n) = map(int, input().split())
(x, y, a) = zip(*[map(int, input().split()) for _ in range(n)])

x_min = 0
x_max = w
y_min = 0
y_max = h

for i in range(n):
    if a[i] == 1:
        x_min = max(x_min, x[i])
    elif a[i] == 2:
        x_max = min(x_max, x[i])
    elif a[i] == 3:
        y_min = max(y_min, y[i])
    else:
        y_max = min(y_max, y[i])

if x_max > x_min:
    x_delta = x_max - x_min
else:
    x_delta = 0
if y_max > y_min:
    y_delta = y_max - y_min
else:
    y_delta = 0
print(x_delta * y_delta)
