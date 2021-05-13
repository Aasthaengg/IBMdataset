

def dis_func(x, y):
    dis = [round(0, 6) for i in range(4)]
    for x, y in zip(x, y):
        tmp = abs(x - y)
        dis[0] += tmp
        dis[1] += (tmp ** 2)
        dis[2] += (tmp ** 3)
        dis[3] = max(dis[3], tmp)

    dis[1] = dis[1] ** (1/2)
    dis[2] = dis[2] ** (1/3)
    print('\n'.join(list(map(str, dis))))


if __name__ == '__main__':
    n = int(input())
    x = list(map(int, input().split()))
    y = list(map(int, input().split()))

    dis_func(x, y)