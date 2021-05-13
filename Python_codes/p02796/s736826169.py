import sys

readline = sys.stdin.readline
MOD = 10 ** 9 + 7
INF = float('INF')
sys.setrecursionlimit(10 ** 5)


def main():
    n = int(readline())
    mat = []

    for _ in range(n):
        x, l = map(int, readline().split())
        left, right = x - l, x + l
        mat.append([left, right])

    mat.sort()

    i = 1
    cur_l, cur_r = mat[0]
    ans = 1

    while i < n:
        next_l, next_r = mat[i]
        if next_l < cur_r:
            if next_r < cur_r:
                cur_l, cur_r = next_l, next_r
        else:
            cur_l, cur_r = next_l, next_r
            ans += 1
        i += 1
    print(ans)


if __name__ == '__main__':
    main()
