n = int(input())
can = True
time = 0
x = 0
y = 0
for _ in range(n):
    t, xx, yy = map(int,input().split())
    distance = abs(x-xx) + abs(y - yy)
    difft = t - time
    if difft < distance:
        can = False
        break
    if (distance - difft) % 2 == 1:
        can = False
        break


    x = xx
    y = yy
    time = t
print("Yes" if can else "No")