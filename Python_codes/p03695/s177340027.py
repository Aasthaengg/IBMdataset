import sys

read = sys.stdin.read
readline = sys.stdin.readline
readlines = sys.stdin.readlines
sys.setrecursionlimit(10 ** 9)
INF = 1 << 60
MOD = 1000000007


def main():
    N, *A = map(int, read().split())

    vec = [0] * 8
    over_red = 0
    for a in A:
        if a >= 3200:
            over_red += 1
        else:
            vec[a // 400] += 1

    c = 0
    for v in vec:
        if v > 0:
            c += 1
    if c > 0:
        print(c, c + over_red)
    else:
        print(1, over_red)

    return


if __name__ == '__main__':
    main()
