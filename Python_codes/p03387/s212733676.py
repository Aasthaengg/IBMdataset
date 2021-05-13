import sys

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline

in_n = lambda: int(readline())
in_nn = lambda: map(int, readline().split())
in_nl = lambda: list(map(int, readline().split()))
in_na = lambda: map(int, read().split())
in_s = lambda: readline().rstrip().decode('utf-8')


def main():
    X = sorted(in_nl())

    A, B, C = X[0], X[1], X[2]

    t = (C - A) + (C - B)
    if t % 2 == 0:
        ans = t // 2
    else:
        C += 1
        A += 1
        ans = ((C - A) + (C - B)) // 2 + 1

    print(ans)


if __name__ == '__main__':
    main()
