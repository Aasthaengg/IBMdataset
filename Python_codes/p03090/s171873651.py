import sys

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

in_n = lambda: int(readline())
in_nn = lambda: map(int, readline().split())
in_s = lambda: readline().rstrip().decode('utf-8')
in_nl = lambda: list(map(int, readline().split()))
in_nl2 = lambda H: [in_nl() for _ in range(H)]
in_map = lambda: [s == ord('.') for s in readline() if s != ord('\n')]
in_map2 = lambda H: [in_map() for _ in range(H)]
in_all = lambda: map(int, read().split())


def main():

    N = in_n()

    ans = []
    for i in range(1, N + 1):
        for j in range(i + 1, N + 1):
            if N % 2 == 0:
                if i + j != N + 1:
                    ans.append((i, j))
            else:
                if i + j != N:
                    ans.append((i, j))

    print(len(ans))
    print('\n'.join(map(lambda a: '{} {}'.format(a[0], a[1]), ans)))


if __name__ == '__main__':
    main()
