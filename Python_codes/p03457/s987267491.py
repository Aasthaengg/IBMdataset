n = int(input())

status = True
t = x = y = 0

for i in range(n):
    ti, xi, yi = list(map(int, input().split()))
    dist = abs(xi-x)+abs(yi-y)
    time = ti-t
    if (dist > time):
        status = False
    elif (time - dist) % 2 == 1:
        status = False

    t, x, y = [ti, xi, yi]

print("Yes" if status else "No")