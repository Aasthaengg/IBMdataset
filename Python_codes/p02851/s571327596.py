import sys

readline = sys.stdin.readline
MOD = 10 ** 9 + 7
INF = float('INF')
sys.setrecursionlimit(10 ** 5)


def main():
    n, k = list(map(int, readline().split()))
    a = [0] + list(map(int, readline().split()))
    from collections import Counter
    b = [0] * (n + 1)

    cur = 0
    for i, x in enumerate(a):
        cur += x
        b[i] = (cur - i) % k

    counter = Counter()
    ans = 0
    for i, x in enumerate(b):
        if i >= k:
            counter[b[i - k]] -= 1
        ans += counter[x]
        counter[x] += 1

    print(ans)


if __name__ == '__main__':
    main()
