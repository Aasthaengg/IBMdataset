import sys
import random

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline

in_n = lambda: int(readline())
in_nn = lambda: map(int, readline().split())
in_nl = lambda: list(map(int, readline().split()))
in_na = lambda: map(int, read().split())
in_s = lambda: readline().rstrip().decode('utf-8')


def query(i):
    print(i)
    sys.stdout.flush()
    s = in_s()

    if s == 'Vacant':
        exit(0)
    elif s == 'Male':
        return 0
    elif s == 'Female':
        return 1


def main():

    N = in_n()

    min_i = 0
    max_i = N

    min_fm = query(0)
    max_fm = min_fm

    while max_i - min_i != 1:
        now_i = (min_i + max_i) // 2
        now_fm = query(now_i)

        if abs(now_i - min_i) % 2 == 0 and now_fm != min_fm:
            max_i = now_i
            max_fm = now_fm
        elif abs(now_i - min_i) % 2 == 1 and now_fm == min_fm:
            max_i = now_i
            max_fm = now_fm
        elif abs(now_i - max_i) % 2 == 0 and now_fm != max_fm:
            min_i = now_i
            min_fm = now_fm
        elif abs(now_i - max_i) % 2 == 1 and now_fm == max_fm:
            min_i = now_i
            min_fm = now_fm


if __name__ == '__main__':
    main()
