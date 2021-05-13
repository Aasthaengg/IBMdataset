import sys

read = sys.stdin.read
readline = sys.stdin.readline
readlines = sys.stdin.readlines
sys.setrecursionlimit(10 ** 9)
INF = 1 << 60
MOD = 1000000007


def main():
    A, B, K = map(int, readline().split())

    vec = []
    for n in range(1, max(A, B) + 1):
        if A % n == 0 and B % n == 0:
            vec.append(n)

    print(vec[-K])
    return


if __name__ == '__main__':
    main()
