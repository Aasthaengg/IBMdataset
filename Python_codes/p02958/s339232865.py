import sys

readline = sys.stdin.readline
MOD = 10 ** 9 + 7
INF = float('INF')
sys.setrecursionlimit(10 ** 5)


def main():
    N = int(readline())
    p = [0] + list(map(int, readline().split()))

    cnt = 0
    for i in range(N + 1):
        if p[i] != i:
            cnt += 1

    if cnt <= 2:
        print("YES")
    else:
        print("NO")


if __name__ == '__main__':
    main()
