import sys
import itertools

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline

in_n = lambda: int(readline())
in_nn = lambda: map(int, readline().split())
in_nl = lambda: list(map(int, readline().split()))
in_na = lambda: map(int, read().split())
in_s = lambda: readline().rstrip().decode('utf-8')


def main():

    S = list(map(int, in_s()))
    N = len(S)
    K = in_n()

    one_i = -1
    for i in range(N):
        if S[i] == 1:
            one_i = i
        else:
            break

    if K <= one_i + 1:
        print(1)
    else:
        ind = min(N - 1, one_i + 1)
        print(S[ind])


if __name__ == '__main__':
    main()
