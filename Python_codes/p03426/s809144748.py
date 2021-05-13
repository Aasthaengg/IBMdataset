import sys

readline = sys.stdin.readline
MOD = 10 ** 9 + 7
INF = float('INF')
sys.setrecursionlimit(10 ** 5)


def main():
    def calc_cost(cur, prev):
        return abs(cur[0] - prev[0]) + abs(cur[1] - prev[1])

    h, w, d = map(int, readline().split())
    a = [list(map(int, readline().split())) for _ in range(h)]
    q = int(readline())
    coordinate = dict()

    for row in range(h):
        for col in range(w):
            num = a[row][col]
            coordinate[num] = (row, col)

    cost = dict()

    for rem in range(1, d + 1):
        cost[rem] = 0
        for num in range(rem + d, h * w + 1, d):
            cost[num] = cost[num - d] + calc_cost(coordinate[num], coordinate[num - d])

    for _ in range(q):
        l, r = map(int, readline().split())
        print(cost[r] - cost[l])


if __name__ == '__main__':
    main()
