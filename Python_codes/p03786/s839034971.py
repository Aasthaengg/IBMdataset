mod = 1000000007
eps = 10**-9


def main():
    import sys
    input = sys.stdin.readline

    N = int(input())
    A = list(map(int, input().split()))
    A.sort()

    S = A[0]
    ans = 1
    for a in A[1:]:
        if S * 2 < a:
            ans = 0
        S += a
        ans += 1
    print(ans)


if __name__ == '__main__':
    main()
