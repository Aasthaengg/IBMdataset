import sys

readline = sys.stdin.readline
MOD = 10 ** 9 + 7
INF = float('INF')
sys.setrecursionlimit(10 ** 5)


def main():
    n = int(readline())
    a = list(map(int, readline().split()))

    i = 0
    ans = 0

    while i < n:
        s = a[i]
        j = i
        k = i
        while j < n and s <= a[j]:
            s = a[j]
            j += 1
        while k < n and s >= a[k]:
            s = a[k]
            k += 1
        i = max(j, k)
        ans += 1

    print(ans)


if __name__ == '__main__':
    main()
