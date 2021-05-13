def main(points):
    points.insert(0, [0, 0, 0])
    for i in range(len(points) - 1):
        p1 = points[i]
        p2 = points[i + 1]
        t = p2[0] - p1[0]
        if not can_reach(p1[1:], p2[1:], t):
            print('No')
            return
    print('Yes')


def can_reach(p1, p2, t):
    length = abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])
    return length <= t and (length - t) % 2 == 0


if __name__ == "__main__":
    points = []
    n = int(input())
    for i in range(n):
        points.append([int(x) for x in input().split(' ')])
    main(points)
