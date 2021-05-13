import sys

sys.setrecursionlimit(10 ** 9)


# map(int, sys.stdin.read().split())


def input():
    return sys.stdin.readline().rstrip()


def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    C = list(map(int, input().split()))
    be = 100
    ans = 0
    for i in A:
        ans += B[i - 1]
        if be == i - 1:
            ans += C[i - 2]
        be = i

    print(ans)


if __name__ == "__main__":
    main()
