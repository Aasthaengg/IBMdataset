import sys

sys.setrecursionlimit(10 ** 8)

input = sys.stdin.readline


def main():
    N, X = [int(x) for x in input().split()]
    A = [int(x) for x in input().split()]

    A.sort()
    ans = 0
    for a in A:
        if X >= a:
            ans += 1
            X -= a

    if X != 0 and ans == N:
        ans -= 1

    print(ans)


if __name__ == '__main__':
    main()
