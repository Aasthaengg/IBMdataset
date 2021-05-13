import sys

readline = sys.stdin.readline
MOD = 10 ** 9 + 7
INF = float('INF')
sys.setrecursionlimit(10 ** 5)


def main():
    cnt = [0] * 4
    for i in range(3):
        a, b = map(int, readline().split())
        a -= 1
        b -= 1
        cnt[a] += 1
        cnt[b] += 1

    if cnt.count(1) == 2 and cnt.count(2) == 2:
        print("YES")
    else:
        print("NO")


if __name__ == '__main__':
    main()
