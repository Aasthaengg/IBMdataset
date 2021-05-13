import sys

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline

in_n = lambda: int(readline())
in_nn = lambda: map(int, readline().split())
in_nl = lambda: list(map(int, readline().split()))
in_na = lambda: map(int, read().split())
in_s = lambda: readline().rstrip().decode('utf-8')


def main():
    S = in_s()
    K = in_n()
    N = len(S)

    subs = set()
    for i in range(N):
        for j in range(1, K + 1):
            if i + j <= N:
                subs |= {S[i:i + j]}

    subs = sorted(subs)
    print(subs[K - 1])


if __name__ == '__main__':
    main()
