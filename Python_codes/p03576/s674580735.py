import sys

readline = sys.stdin.readline
MOD = 10 ** 9 + 7
INF = float('INF')
sys.setrecursionlimit(10 ** 5)


def main():
    from itertools import combinations
    from operator import itemgetter
    n, k = map(int, readline().split())
    points = [list(map(int, readline().split())) for _ in range(n)]

    points.sort(key=itemgetter(0))
    for i in range(n):
        points[i].append(i)
    points.sort(key=itemgetter(1))
    for i in range(n):
        points[i].append(i)

    points.sort(key=itemgetter(2))

    ans = INF

    for first, last in combinations(range(n), 2):
        if (last - first + 1) < k:
            continue
        for p, q in combinations(range(first, last + 1), 2):
            gn = max(points[p][3],points[q][3])
            ln = min(points[p][3],points[q][3])
            count = 0

            for x, y, xn, yn in points:
                if first <= xn <= last and ln <= yn <= gn:
                    count += 1
            if count >= k:
                width = abs(points[last][0] - points[first][0])
                height = abs(points[p][1] - points[q][1])
                area = width * height
                ans = min(ans, area)
    print(ans)


if __name__ == '__main__':
    main()
