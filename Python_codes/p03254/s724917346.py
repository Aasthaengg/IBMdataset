mod = 1000000007
eps = 10**-9


def main():
    import sys
    input = sys.stdin.readline

    N, X = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()

    if sum(A) == X:
        print(N)
    else:
        ans = 0
        for a in A[:-1]:
            if a <= X:
                ans += 1
                X -= a
            else:
                break
        print(ans)


if __name__ == '__main__':
    main()
