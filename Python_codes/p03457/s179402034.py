n = int(input())
t = [0] * (n + 1)
x = [0] * (n + 1)
y = [0] * (n + 1)
for i in range(n):
    t[i+1], x[i+1], y[i+1] = map(int, input().split())

can = True
for i in range(n):
    dt = t[i+1] -t[i]
    dist = abs(x[i+1] - x[i]) + abs(y[i+1] - y[i])
    if dt < dist:
        can = False
    # ここはよくわかっていない
    if dist % 2 != dt % 2:
        can = False
if can:
    print("Yes")
else:
    print("No")