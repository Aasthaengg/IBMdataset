a, b = map(int, input().split())
tap = 1
x = 0
while True:
    if tap < b:
        x += 1
        tap += (a - 1)
    else:
        print(x)
        exit()
