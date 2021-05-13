from itertools import combinations


def main():
    N = int(input())
    points = [list(map(int, input().split())) for _ in range(N)]
    ans = N
    for i, j in combinations(range(N), 2):
        p1, p2 = points[i], points[j]
        if p1 == p2:
            continue
        dx, dy = p1[0] - p2[0], p1[1] - p2[1]
        cost = N
        for k, l in combinations(range(N), 2):
            p3, p4 = points[k], points[l]
            if (p3[0] + dx == p4[0] and p3[1] + dy == p4[1]) or \
                    (p4[0] + dx == p3[0] and p4[1] + dy == p3[1]):
                cost -= 1
        ans = min(ans, cost)
    print(ans)


if __name__ == '__main__':
    main()
