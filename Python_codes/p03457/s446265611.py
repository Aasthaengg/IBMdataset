N = int(input())
t = [0] * (N + 1)
x = [0] * (N + 1)
y = [0] * (N + 1)
for i in range(N):
    t[i + 1], x[i + 1], y[i + 1] = map(int, input().split())
for i in range(N):
    dt = t[i + 1] - t[i]
    dst = abs(x[i + 1] - x[i]) + abs(y[i + 1] - y[i])
    if (dt < dst) or (dt % 2 != dst % 2):
        print("No")
        break
else:
    print("Yes")