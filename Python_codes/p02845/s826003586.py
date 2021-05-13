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

    mod = 10**9 + 7
    num = [0] * 3
    ans = 1

    for i in range(N):
        min_j = 4
        count = 0
        for j in range(3):
            if num[j] == A[i]:
                count += 1
                min_j = min(min_j, j)
        if min_j == 4:
            ans = 0
            break
        num[min_j] += 1
        ans *= count
        ans %= mod

    print(ans)


if __name__ == '__main__':
    main()
