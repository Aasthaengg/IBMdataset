while True:
    [n, m] = [int(x) for x in raw_input().split()]
    if [n, m] == [0, 0]:
        break

    hoge = range(1, n + 1)

    data = []
    for x in range(0, n - 2):
        for y in range(x + 1, n - 1):
            for z in range(y + 1, n):
                s = hoge[x] + hoge[y] + hoge[z]
                if s == m:
                    data.append(s)

    print(len(data))