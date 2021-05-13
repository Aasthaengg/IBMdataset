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
    a = list(in_na())

    t = 0
    for i in range(N):
        t = t | a[i]

    if t % 2 == 0:
        print('second')
    else:
        print('first')


if __name__ == '__main__':
    main()
