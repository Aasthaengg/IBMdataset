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
    A = in_nl()

    ans = 0
    for a in A:
        while a:
            if a % 2 == 0:
                a //= 2
                ans += 1
            else:
                break

    print(ans)


if __name__ == '__main__':
    main()
