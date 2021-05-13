import sys

read = sys.stdin.read
readline = sys.stdin.readline
readlines = sys.stdin.readlines
sys.setrecursionlimit(10 ** 9)
INF = 1 << 60
MOD = 1000000007


def main():
    N = int(readline())
    vec = [0] * (N + 1)
    vec[0] = 2
    vec[1] = 1

    for i in range(2, N + 1):
        vec[i] = vec[i - 1] + vec[i - 2]

    print(vec[N])
    return


if __name__ == '__main__':
    main()
