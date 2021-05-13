import sys

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline

in_n = lambda: int(readline())
in_nn = lambda: map(int, readline().split())
in_s = lambda: readline().rstrip().decode('utf-8')


def main():

    A, B, C = in_nn()
    ans = min(B // A, C)
    print(ans)


if __name__ == '__main__':
    main()
