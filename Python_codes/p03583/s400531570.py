import sys

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline

in_n = lambda: int(readline())
in_nn = lambda: map(int, readline().split())
in_nl = lambda: list(map(int, readline().split()))
in_na = lambda: map(int, read().split())
in_s = lambda: readline().rstrip().decode('utf-8')


def main():
    N = in_n()

    for a in range(1, 3500):
        for b in range(a, 3500):
            t1 = N * a * b
            t2 = 4 * a * b - N * (a + b)
            if t2 == 0:
                continue
            else:
                c = t1 / t2
                if c.is_integer() and 1 <= c:
                    print(a, b, int(c))
                    exit()


if __name__ == '__main__':
    main()
