a, b, c = map(int, input().split())

cnt = 0

while True:
    if a % 2 == 1:
        print(cnt)
        exit()
    if b % 2 == 1:
        print(cnt)
        exit()
    if c % 2 == 1:
        print(cnt)
        exit()
    if a == b and a == c:
        print(-1)
        exit()
    lis = []
    lis.append((b+c)/2)
    lis.append((a+c)/2)
    lis.append((a+b)/2)
    a, b, c = lis

    cnt += 1