import sys

readline = sys.stdin.readline
MOD = 10 ** 9 + 7
INF = float('INF')
sys.setrecursionlimit(10 ** 5)


def main():
    from itertools import accumulate

    n = int(readline())
    a = list(map(int, readline().split()))
    ans = 0

    sum_cur = 0
    xor_cur = 0
    idx = 0

    for i, x in enumerate(a):
        sum_cur += x
        xor_cur ^= x

        while idx <= i:
            if sum_cur == xor_cur:
                ans += (i + 1) - idx
                break
            else:
                sum_cur -= a[idx]
                xor_cur ^= a[idx]
                idx += 1

    print(ans)


if __name__ == '__main__':
    main()
