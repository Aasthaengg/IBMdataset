import sys
from itertools import accumulate

read = sys.stdin.read
readline = sys.stdin.readline
readlines = sys.stdin.readlines
sys.setrecursionlimit(10 ** 9)
INF = 1 << 60
MOD = 1000000007


def main():
    W, H, N, *XYA = map(int, read().split())

    vec_x = [0] * (W + 1)
    vec_y = [0] * (H + 1)
    for x, y, a in zip(*[iter(XYA)] * 3):
        if a == 1:
            vec_x[0] += 1
            vec_x[x] -= 1
        elif a == 2:
            vec_x[x] += 1
            vec_x[W] -= 1
        elif a == 3:
            vec_y[0] += 1
            vec_y[y] -= 1
        else:
            vec_y[y] += 1
            vec_y[H] -= 1

    vec_x = list(accumulate(vec_x))
    vec_y = list(accumulate(vec_y))

    ans = 0
    for i in range(W):
        for j in range(H):
            if vec_x[i] == 0 and vec_y[j] == 0:
                ans += 1

    print(ans)
    return


if __name__ == '__main__':
    main()
