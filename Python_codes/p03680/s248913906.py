n = int(input())
a = [0] * (n + 1)

for i in range(1, n+1):
    a[i] = int(input())

cnt = 0
light = 1
push = [0] * (n+1)

for i in range(1, len(a) + 1):
    if push[light] == 0:
        push[light] = 1
        light = a[light]
        cnt += 1
        if light == 2:
            print(cnt)
            exit()
    else:
        print(-1)
        exit()
