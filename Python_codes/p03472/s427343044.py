import sys

readline = sys.stdin.readline
MOD = 10 ** 9 + 7
INF = float('INF')
sys.setrecursionlimit(10 ** 5)


def main():
    n, h = map(int, readline().split())
    a = [0] * n
    b = [0] * n

    for i in range(n):
        a[i], b[i] = map(int, readline().split())

    a_max = max(a)
    b.sort(reverse=True)
    rem = h

    ans = 0

    for x in b:
        if x >= a_max:
            rem -= x
            ans += 1
            if rem <= 0:
                break
        else:
            break
    if rem > 0:
        ans += (rem + a_max - 1) // a_max
    print(ans)


if __name__ == '__main__':
    main()
