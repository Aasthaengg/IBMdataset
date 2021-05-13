def main():
    N, K = (int(i) for i in input().split())
    A = [int(i) for i in input().split()]
    A.sort()
    maxA = A.pop()
    if maxA < K:
        return print("IMPOSSIBLE")
    if N == 1:
        if maxA == K:
            return print("POSSIBLE")
        else:
            return print("IMPOSSIBLE")
    g = A[0]

    def gcd(x, y):
        if y == 0:
            return x
        while y != 0:
            x, y = y, x % y
        return x

    for a in A[1:]:
        g = gcd(g, a)

    if (maxA - K) % g == 0:
        print("POSSIBLE")
    else:
        print("IMPOSSIBLE")


if __name__ == '__main__':
    main()
