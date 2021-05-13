import sys

readline = sys.stdin.readline
MOD = 10 ** 9 + 7
INF = float('INF')
sys.setrecursionlimit(10 ** 5)


def main():
    n = int(readline())
    points = [int(readline()) for _ in range(n)]
    points.sort()
    ans = sum(points)

    if ans % 10 == 0:
        flag = False
        for point in points:
            if point % 10 != 0:
                ans -= point
                flag = True
                break
        if not flag:
            ans = 0

    print(ans)


if __name__ == '__main__':
    main()
