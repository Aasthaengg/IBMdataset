import sys

read = sys.stdin.read
readline = sys.stdin.readline
readlines = sys.stdin.readlines
sys.setrecursionlimit(10 ** 9)
INF = 1 << 60
MOD = 1000000007


def main():
    N, *A = map(int, read().split())

    ans = 0
    while True:
        ok = True
        for i in range(N):
            if A[i] % 2 == 0:
                A[i] //= 2
            else:
                ok = False
        if ok:
            ans += 1
        else:
            break

    print(ans)
    return


if __name__ == '__main__':
    main()
