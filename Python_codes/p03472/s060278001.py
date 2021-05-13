import sys
from collections import deque

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline

in_n = lambda: int(readline())
in_nn = lambda: map(int, readline().split())
in_nl = lambda: list(map(int, readline().split()))
in_na = lambda: map(int, read().split())
in_s = lambda: readline().rstrip().decode('utf-8')


def main():

    N, H = in_nn()
    ab = []
    for i in range(N):
        a, b = in_nn()
        ab.append((a, 0))
        ab.append((b, 1))

    ab = deque(sorted(ab, reverse=True))

    count = 0
    while H > 0:
        d, x = ab.popleft()
        if x == 1:
            H -= d
            count += 1
        else:
            count += -(-H // d)
            break

    print(count)


if __name__ == '__main__':
    main()
