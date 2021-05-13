if __name__ == '__main__':

    N = int(input())
    x = []
    y = []

    for _ in range(N):
        x_, y_ = map(int, input().split())
        x.append(x_)
        y.append(y_)
    xpy = [a + b for a, b in zip(x, y)]
    xmy = [a - b for a, b in zip(x, y)]
    max_1 = max(xpy)
    min_1 = min(xpy)
    max_2 = max(xmy)
    min_2 = min(xmy)
    print(max(max_1 - min_1,max_2 - min_2))


