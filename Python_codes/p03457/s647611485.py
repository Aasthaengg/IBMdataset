n = int(input())
t = [0 for i in range(n)]
x = [0 for i in range(n)]
y = [0 for i in range(n)]
for i in range(n):
    t[i], x[i], y[i] = list(map(int, input().split()))

t_0 = 0
x_0 = 0
y_0 = 0

can = True

dt = t[0] - t_0
dx = x[0] - x_0
dy = y[0] - y_0
dist = abs(dx) + abs(dy)

if dt >= dist and dt % 2 == dist % 2:
    can = True
else:
    can = False

for i in range(1, n):
    dt = t[i] - t[i - 1]
    dx = x[i] - x[i - 1]
    dy = y[i] - y[i - 1]
    dist = abs(dx) + abs(dy)
    if dt >= dist and dt % 2 == dist % 2:
        can = True
    else:
        can = False
        break

if can:
    print("Yes")
else:
    print("No")

pass
