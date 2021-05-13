import sys

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline

in_n = lambda: int(readline())
in_nn = lambda: map(int, readline().split())
in_s = lambda: readline().rstrip().decode('utf-8')


def main():

    S = list(map(int, in_s()))
    ans = min(S.count(0), S.count(1))
    print(ans * 2)


if __name__ == '__main__':
    main()
