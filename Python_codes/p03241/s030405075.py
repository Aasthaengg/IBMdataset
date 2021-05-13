import sys

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline

in_n = lambda: int(readline())
in_nn = lambda: map(int, readline().split())
in_s = lambda: readline().rstrip().decode('utf-8')


def main():
    N, M = in_nn()

    ans = 1
    inf = M // N + 1
    for i in range(inf, 1, -1):
        if i * N <= M and M % i == 0:
            ans = i
            break

    print(ans)


if __name__ == '__main__':
    main()
