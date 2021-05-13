import math

def resolve():
    N, D = map(int, input().split())
    count = 0

    for i in range(N):
        a, b = map(int, input().split())
        ans = math.sqrt(a ** 2 + b ** 2)
        if ans <= D:
            count += 1
    print(count)
resolve()