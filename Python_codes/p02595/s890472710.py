


def dist(point):
    return (point[0]**2 + point[1]**2)**(1/2)


if __name__ == "__main__" :
    N,D = [int(i) for i in input().split()]
    count = 0
    for _ in range(N):
        point = [int(i) for i in input().split()]
        if dist(point) <= D:
            count += 1

    print(count)
