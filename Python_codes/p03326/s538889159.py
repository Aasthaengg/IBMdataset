import sys

readline = sys.stdin.readline
MOD = 10 ** 9 + 7
INF = float('INF')
sys.setrecursionlimit(10 ** 5)


def main():
    n, m = map(int, readline().split())
    mat = [list(map(int, readline().split())) for _ in range(n)]

    from itertools import product
    from operator import itemgetter

    ans = 0

    for bit in product([-1, 1], repeat=3):
        cake_value = [[0] * 2 for _ in range(n)]
        for i, row in enumerate(mat):
            cake_value[i][0] = i
            cake_value[i][1] = row[0] * bit[0] + row[1] * bit[1] + row[2] * bit[2]
        cake_value.sort(key=itemgetter(1), reverse=True)
        x_sum, y_sum, z_sum = [0] * 3
        for i, _ in cake_value[:m]:
            cake = mat[i]
            x_sum += mat[i][0]
            y_sum += mat[i][1]
            z_sum += mat[i][2]
        total = abs(x_sum) + abs(y_sum) + abs(z_sum)
        ans = max(ans, total)

    print(ans)


if __name__ == '__main__':
    main()
