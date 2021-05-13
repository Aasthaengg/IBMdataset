a, b = map(int, input().split())

if a % b == 0:
    print(-1)
else:
    for i in range(1, a*b+1):
        if (a * i) % b != 0:
            print(a * i)
            break