import sys

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

in_n = lambda: int(readline())
in_nn = lambda: map(int, readline().split())
in_s = lambda: readline().rstrip().decode('utf-8')
in_nl = lambda: list(map(int, readline().split()))
in_nl2 = lambda H: [in_nl() for _ in range(H)]
in_map = lambda: [s == ord('.') for s in readline() if s != ord('\n')]
in_map2 = lambda H: [in_map() for _ in range(H)]
in_all = lambda: map(int, read().split())


def main():

    N = in_n()
    A = list(in_all())

    if N == 0:
        if A[0] == 0:
            print(0)
            exit()
        else:
            print(-1)
            exit()

    if A[0] != 0:
        print(-1)
        exit()

    ans = 0
    for i in range(N - 1):
        if A[i] < A[i + 1]:
            if A[i + 1] - A[i] == 1:
                ans += 1
            else:
                print(-1)
                exit()
        elif A[i] >= A[i + 1]:
            ans += A[i + 1]

    print(ans)


if __name__ == '__main__':
    main()
