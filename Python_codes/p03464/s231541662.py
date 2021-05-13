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

    K = in_n()
    A = in_nl()[::-1]

    min_n = 2
    max_n = 2

    for group in A:

        cnt = -(-min_n // group)
        next_min = group * cnt
        if not (min_n <= next_min <= max_n):
            print(-1)
            exit()

        cnt = max_n // group
        next_max = cnt * group + (group - 1)

        min_n, max_n = next_min, next_max

    print(min_n, max_n)


if __name__ == '__main__':
    main()
