import sys

read = sys.stdin.read
readline = sys.stdin.readline
readlines = sys.stdin.readlines
sys.setrecursionlimit(10 ** 9)
INF = 1 << 60
MOD = 1000000007


def main():
    W, a, b = map(int, readline().split())

    if a <= b <= a + W or a <= b + W <= a + W:
        ans = 0
    else:
        ans = min(abs(a - b), abs(a + W - b), abs(a - b - W), abs(a + W - b - W))

    print(ans)

    return


if __name__ == '__main__':
    main()
