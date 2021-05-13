a, b, c = map(int, input().split())

times = 0
if a == b and b == c and a % 2 == 0:
    print(-1)
else:
    while 1:
        if a % 2 == 1 or b % 2 == 1 or c % 2 == 1:
            break
        a, b, c = int((b + c)/2), int((c + a)/2), int((a + b)/2)
        times += 1

    print(times)