import sys


def solve():
    input = sys.stdin.readline
    mod = 10 ** 9 + 7
    n, k = list(map(int, input().rstrip('\n').split()))
    if k <= (n - 1) * (n - 2) // 2:
        t = n - 1 + ((n - 1) * (n - 2)) // 2 - k
        print(t)
        cnt = 0
        for i in range(2, n + 1):
            print(1, i)
            cnt += 1
        for i in range(2, n + 1):
            for j in range(i + 1, n + 1):
                if cnt == t:
                    exit()
                print(i, j)
                cnt += 1
    else:
        print(-1)


if __name__ == '__main__':
    solve()
