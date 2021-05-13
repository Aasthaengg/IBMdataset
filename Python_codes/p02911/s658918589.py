def resolve():
    n, k, q = map(int, input().split())
    points = [k] * n
    for _ in range(q):
        temp = int(input())
        points[temp - 1] += 1
    points = map(lambda x: x - q, points)
    for i in points:
        if i <= 0:
            print('No')
            continue
        print('Yes')
resolve()