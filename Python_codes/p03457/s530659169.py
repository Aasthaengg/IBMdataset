I = int(input())

pt = px = py = 0
for i in range(I):
    t, x, y = map(int, input().split())

    costtime = abs(t - pt)
    distance = abs(x - px) + abs(y - py)

    if costtime%2 != distance%2:
        print("No")
        exit()

    if costtime < distance:
        print("No")
        exit()

    pt,px,py = t,x,y

print("Yes")
