import sys

readline = sys.stdin.readline
MOD = 10 ** 9 + 7
INF = float('INF')
sys.setrecursionlimit(10 ** 5)


def main():
    n = int(readline())
    mat = []
    for _ in range(n):
        a, b = map(int, readline().split())
        c = a + b
        mat.append([c, a, b])

    mat.sort(reverse=True)

    a_sum, b_sum = 0, 0

    for i in range(n):
        if i % 2 == 0:
            a_sum += mat[i][1]
        else:
            b_sum += mat[i][2]

    print(a_sum - b_sum)


if __name__ == '__main__':
    main()
