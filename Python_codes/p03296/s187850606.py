mod = 1000000007
eps = 10**-9


def main():
    import sys
    input = sys.stdin.readline

    N = int(input())
    A = list(map(int, input().split()))

    ans = 0
    for i in range(1, N):
        if A[i] == A[i-1]:
            A[i] = 0
            ans += 1
    print(ans)


if __name__ == '__main__':
    main()
