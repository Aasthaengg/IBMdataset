import sys

readline = sys.stdin.readline
MOD = 10 ** 9 + 7
INF = float('INF')
sys.setrecursionlimit(10 ** 5)


def main():
    k, t = map(int, readline().split())
    a = list(map(int, readline().split()))
    ans = 0
    prev = -1

    for _ in range(k):
        max_a = 0
        cur = -1
        for i in range(t):
            if i != prev:
                if a[i] > max_a:
                    max_a = a[i]
                    cur = i
        if cur != -1:
            a[cur] -= 1
            prev = cur

    print(sum(a))


if __name__ == '__main__':
    main()
