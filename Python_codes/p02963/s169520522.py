import sys

input = sys.stdin.readline


def main():
    S = int(input())

    # X2*Y3-X3*Y2 = S
    #   (X2,Y2) = (10**9,1)
    # 10**9*Y3 - X3 = S
    # S = 10**9*q + r
    #   = 10**9*(q+1) - (10**9-r)
    # (X3,Y3) = (10**9-r, q+1)
    q, r, = divmod(S, 10**9)
    if r == 0:
        X = 0
        Y = q
    else:
        X = 10**9 - r
        Y = q + 1
    ans = [0, 0, 10**9, 1, X, Y]
    print(*ans)


if __name__ == "__main__":
    main()
