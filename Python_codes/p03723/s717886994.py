a, b, c = map(int, input().split())
if a == b == c:
    if a % 2 == 0:
        print(-1)
        exit()
    else:
        print(0)
        exit()
for i in range(0, 10**6):
    if a % 2 == 1 or b % 2 == 1 or c % 2 == 1:
        print(i)
        exit()
    a, b, c = (b+c) / 2, (c+a)/2, (a+b)/2
