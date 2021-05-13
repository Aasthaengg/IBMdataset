N = int(input())
t, x, y = 0, 0, 0
for i in range(N):
    t_i, x_i, y_i = map(int, input().split())
    T = t_i-t
    D = abs(x_i-x) + abs(y_i-y)
    if T % 2 != D % 2 or D > T:
        print("No")
        exit()
    else:
        t = t_i
        x = x_i
        y = y_i
print("Yes")