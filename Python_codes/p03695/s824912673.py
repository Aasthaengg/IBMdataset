n = int(input())
a = list(map(int, input().split()))

color = [False]*8
flex = 0
cnt = 0
for i in range(n):
    if a[i] < 400:
        color[0] = True
    elif a[i] < 800:
        color[1] = True
    elif a[i] < 1200:
        color[2] = True
    elif a[i] < 1600:
        color[3] = True
    elif a[i] < 2000:
        color[4] = True
    elif a[i] < 2400:
        color[5] = True
    elif a[i] < 2800:
        color[6] = True
    elif a[i] < 3200:
        color[7] = True
    else:
        flex += 1

for i in range(8):
    if color[i]:
        cnt += 1
mi = cnt
if mi == 0:
    mi = 1
cnt += flex

print(str(mi) + " " + str(cnt))
