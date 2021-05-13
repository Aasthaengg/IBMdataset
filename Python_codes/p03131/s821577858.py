import sys

sys.setrecursionlimit(10 ** 8)

input = sys.stdin.readline


def main():
    K, A, B = [int(x) for x in input().split()]

    if B - A <= 2 or K <= A:
        print(K + 1)
        return
    ans = A
    K -= (A - 1)
    ans += (K // 2) * (B - A)
    ans += K % 2
    print(ans)


if __name__ == '__main__':
    main()
