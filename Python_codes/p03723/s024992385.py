def f(a, b, c):
    if a > 1 and a == b and a == c:
        print(-1)
    else:
        count = 0
        for i in range(100):
            if a%2 or b%2 or c%2:
                break
            a, b, c = b//2 + c//2, a//2 + c//2, a//2 + b//2
            count += 1
        print(count)

a, b, c = map(int, input().split())
f(a, b, c)
