x, y = map(int,input().split())

cnt = 0
while True:
    if y >= x:
        cnt += 1
        y = y // 2
    else:
        print(cnt)
        exit()
