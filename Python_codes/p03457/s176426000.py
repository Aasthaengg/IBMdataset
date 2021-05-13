n = int(input())
t = [0] * n
x = [0] * n
y = [0] * n
for i in range(n):
    t[i], x[i], y[i] = map(int, input().split())

x_defo = 0
y_defo = 0
t_defo = 0
result = 0

for i in range(n):
    dt = t[i] - t_defo
    it = abs(x[i]-x_defo) + abs(y[i]-y_defo)
    if it > dt:
        result = 1
        break
    if it %2 != dt %2:
        result = 1
        break
    else:
        x_defo = x[i]
        y_defo = y[i]
        t_defo = t[i]

if result ==0:
    print("Yes")
else:
    print("No")
