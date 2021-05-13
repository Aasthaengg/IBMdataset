mod = 1000000007
eps = 10**-9


def main():
    import sys
    input = sys.stdin.readline

    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    ans = 0
    P = []
    v = 0
    for a, b in zip(A, B):
        if a >= b:
            P.append(a - b)
        else:
            v += b-a
            ans += 1
    P.sort(reverse=True)

    for p in P:
        if v <= 0:
            break
        v -= p
        ans += 1
    if v <= 0:
        print(ans)
    else:
        print(-1)


if __name__ == '__main__':
    main()
